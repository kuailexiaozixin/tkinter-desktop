# 06 数据层（sqlite3 标准库）

> 本技能数据层默认用标准库 `sqlite3`：单文件、打包无坑；复杂/多实体场景可用 SQLAlchemy（见 `examples/README.md` 末尾「真实案例研究」案例 1）。
> 不引入 ORM（SQLAlchemy 等）——桌面工具场景收益低、体积代价大。

## 连接管理

```python
import sqlite3
from .config import DATA_DIR

DB_PATH = DATA_DIR / "app.db"

def get_conn() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row          # 行为 dict-like，r["name"] 可用
    conn.execute("PRAGMA foreign_keys = ON")  # 默认是关的，必须每连接打开
    return conn
```

- 桌面单用户场景：**App 级单连接 + 主线程独占**最简单可靠；
  需要 worker 线程写库时，在 worker 内 `get_conn()` 新开连接用完即关
- `conn.execute(...)` 后写操作必须 `conn.commit()`；批量导入用
  `with conn:`（自动事务）+ `executemany`

## Schema 与迁移

```python
SCHEMA_VERSION = 3

def init_db(conn):
    conn.executescript(DDL)                    # CREATE TABLE IF NOT EXISTS ...
    ver = conn.execute("PRAGMA user_version").fetchone()[0]
    for upgrade in MIGRATIONS[ver:]:           # [(v1->v2 的函数), (v2->v3), ...]
        upgrade(conn)
    conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
    conn.commit()
```

- 版本号存 `PRAGMA user_version`，比自建 meta 表干净
- DDL 全部 `IF NOT EXISTS`，可幂等重跑
- **种子数据幂等**：`INSERT OR IGNORE`（配唯一索引）或先 `SELECT COUNT(*)` 判空再插

> **两种建库策略**（按项目成熟度选）：
> - **简单应用 / 首版**：直接 `conn.executescript(SCHEMA)`，
>   `SCHEMA` 全是 `CREATE TABLE IF NOT EXISTS`，**每次启动重跑即幂等**，
>   无需 user_version 迁移——零维护、零出错。
> - **schema 需要演进**（加列 / 改约束 / 多版升级）：才上 `PRAGMA user_version`
>   + `MIGRATIONS` 增量迁移（见上方示例）。也可用 `ALTER TABLE` 兜底旧库缺列。

## Repository 模式

```python
class ProjectRepo:
    def __init__(self, conn): self.conn = conn

    def list(self, keyword: str = "") -> list[sqlite3.Row]:
        sql = "SELECT * FROM project WHERE name LIKE ? ORDER BY id DESC"
        return self.conn.execute(sql, (f"%{keyword}%",)).fetchall()

    def create(self, data: dict) -> int:
        cur = self.conn.execute(
            "INSERT INTO project(code, name, boundary, status) VALUES(?,?,?,?)",
            (data["code"], data["name"], data["boundary"], "进行中"))
        self.conn.commit()
        return cur.lastrowid
```

- **值必须 `?` 参数化（防注入）**；但**标识符（表名 / 列名 / `ORDER BY` / `LIMIT`）无法用 `?` 绑定**
  ——`SELECT * FROM ?` 会直接报 `OperationalError`（已运行核实）。标识符只能受控拼接：
  来自代码内部常量（如 `repository` 函数参数里的 `"project"`）可用 f-string；
  **绝不可**把用户输入拼进表名 / 列名。正例如下：`repository` 函数把表名 / 列名写成
  受控硬编码常量，值全 `?` 参数化，安全可查。
- 返回 `sqlite3.Row` 或转 dict，不要返回裸 tuple（列序变更即炸）
- 领域计算（归集、报表汇总）放 `services.py`，Repo 只做存取；
  聚合报表优先一条 SQL `GROUP BY` 解决，别取全量到 Python 里循环

## 与 GUI 协作的约定

- View/Controller 不写 SQL；Controller 只调 Repo/Service 方法
- 写操作成功 → Controller 调 `view.refresh()` + 状态栏提示；失败 →
  `messagebox.showerror`，并把异常写日志
- 金额一律以"分"存整数或 REAL + 显示层格式化；日期存 ISO 文本 `YYYY-MM-DD`
  （sqlite 无日期类型，ISO 文本可直接字符串比较排序）

## 示例：数据层（示意）

App 级单连接工厂（与 `05` 线程 nuance 的模式 C 对应）：

```python
_conn: sqlite3.Connection | None = None

def get_conn() -> sqlite3.Connection:
    global _conn
    if _conn is None:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        _conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)  # 单连接跨线程用
        _conn.row_factory = sqlite3.Row
        _conn.execute("PRAGMA foreign_keys=ON")      # 默认关（已核实=0），每连接打开
        _create_schema(_conn)                        # executescript(CREATE TABLE IF NOT EXISTS)
    return _conn

@contextmanager
def tx():                                            # 自管事务：成功 commit / 异常 rollback
    conn = get_conn()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
```

- `check_same_thread=False` + 单连接：配合 `_busy` 单 worker 串行访问（见 `05`），
  **不是**靠它获得线程安全，而是靠串行化；多 worker 并发必须加 `threading.Lock`。
- `foreign_keys` 默认关闭（运行核实默认 `=0`），此处每连接显式 `ON`。
- `tx()` 上下文管理器比裸 `with conn:` 更清晰，异常自动回滚。
- `row_factory = sqlite3.Row`，`repository.py` 取数后转 `dict(r)` 返回，避免裸 tuple。

`models/repository.py` 的标识符拼接（正确姿势）：

```python
def rows(table, where="", params=(), order="id"):
    sql = f"SELECT * FROM {table}"          # 表名来自函数参数（硬编码常量），非用户输入
    if where: sql += f" WHERE {where}"
    if order: sql += f" ORDER BY {order}"
    return [dict(r) for r in get_conn().execute(sql, params).fetchall()]  # 值全 ? 参数化
```

值一律 `?` 参数化；表名 / 列名 / `ORDER BY` 来自内部常量，f-string 拼接安全。
用户输入只经 `params` 进入，杜绝注入。

## 打包与路径

- DB 文件放 EXE 同级 `data/` 目录（`config.py` 里 `sys.frozen` 适配），
  **绝不能放进打包资源**（_MEIPASS 是只读临时目录，写库必失败且退出即丢）
- 首启自动建库建表 + 种子数据，用户零配置
- WAL 模式（`PRAGMA journal_mode=WAL`）在单用户桌面场景非必需；
  开了会多出 -shm/-wal 文件，交付拷贝数据库时容易漏——默认不开
