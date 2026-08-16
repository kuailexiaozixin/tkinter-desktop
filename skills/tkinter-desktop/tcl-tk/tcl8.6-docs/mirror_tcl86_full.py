#!/usr/bin/env python3
"""Mirror the Tcl8.6 / Tk8.6 command reference (all 16 sections) from tcl-lang.org.

Scope: ALL official sections of the Tcl 8.6.18/Tk 8.6.18 docs:
    UserCmd, TclCmd, TkCmd, ItclCmd, SqliteCmd, TdbcCmd,
    TdbcmysqlCmd, TdbcodbcCmd, TdbcpostgresCmd, TdbcsqliteCmd, ThreadCmd,
    TclLib, TkLib, ItclLib, TdbcLib, Keywords.

Output: Markdown (`.md`) — HTML converted via html2text, starting from the
NAME heading (skipping breadcrumb + top nav), cross-links rewritten .htm->.md.
Incremental: skips pages whose .md already exists (keeps existing high-quality
TclCmd/TkCmd pages untouched).
"""
import os
import re
import sys
import time
import urllib.request
import urllib.error
from urllib.parse import urljoin, urlparse

BASE = "https://www.tcl-lang.org/man/tcl8.6"
OUT = os.path.dirname(os.path.abspath(__file__))

# All 16 official sections (from official top-level contents.htm)
SECTIONS = [
    "UserCmd", "TclCmd", "TkCmd", "ItclCmd", "SqliteCmd", "TdbcCmd",
    "TdbcmysqlCmd", "TdbcodbcCmd", "TdbcpostgresCmd", "TdbcsqliteCmd",
    "ThreadCmd", "TclLib", "TkLib", "ItclLib", "TdbcLib", "Keywords",
]

HREF_RE = re.compile(r'href\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
# 正文起点：第一个正文标题 NAME（面包屑 H2 + 顶部导航 H3 之前的最后一个 H3）
NAME_RE = re.compile(r'<H3><A NAME="M2">NAME</A></H3>', re.IGNORECASE)
NAME_RE2 = re.compile(r'<H3[^>]*>\s*(?:<A[^>]*>\s*)?NAME\s*(?:</A>)?\s*</H3>', re.IGNORECASE)


def fetch(url, retries=3):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            return data
        except Exception as e:
            last = e
            time.sleep(1.2)
    raise RuntimeError(f"fetch failed: {url}: {last}")


def html_to_md(raw: bytes) -> str:
    """Convert a single man-page HTML to Markdown, starting at the NAME heading."""
    try:
        import html2text
    except ImportError:
        print("!! html2text not installed — run: pip install html2text")
        sys.exit(1)
    text = raw.decode("utf-8", errors="replace")
    m = NAME_RE.search(text)
    if not m:
        m = NAME_RE2.search(text)
    start = m.start() if m else 0
    seg = text[start:]
    h = html2text.HTML2Text()
    h.body_width = 79
    h.emphasis_mark = "*"
    h.unicode_snob = True
    h.ignore_images = True
    h.ignore_emphasis = False
    md = h.handle(seg)
    # 交叉链接 .htm -> .md
    md = re.sub(r'\.htm(?=[)"\s])', ".md", md)
    # 去掉 href 中可能的 ../ 上级链接外的多余锚点（保留相对引用）
    return md.strip() + "\n"


def save_md(relpath, content):
    full = os.path.join(OUT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def is_local_page(href):
    if not href:
        return False
    low = href.lower()
    if low.startswith("http://") or low.startswith("https://"):
        return False
    if low.startswith("mailto:") or low.startswith("javascript:"):
        return False
    if "#" in low:
        low = low.split("#", 1)[0]
    if not low:
        return False
    return low.endswith(".htm") or low.endswith(".html")


def normalize(href):
    return href.split("#", 1)[0]


def collect_pages_in_section(sec, index_html):
    """Collect command page filenames inside this section from its contents.htm."""
    pages = set()
    for href in HREF_RE.findall(index_html):
        if not is_local_page(href):
            continue
        href = normalize(href)
        resolved = urljoin(f"{BASE}/{sec}/", href)
        path = urlparse(resolved).path
        marker = f"/man/tcl8.6/{sec}/"
        idx = path.find(marker)
        if idx != -1:
            local = path[idx + len(marker):]
            if local and is_local_page(local):
                if local.lower() in ("contents.htm", "contents.html"):
                    continue
                pages.add(local)
    return sorted(pages)


def gen_contents_md(sec, pages, ok_set, fail_set):
    """Generate <sec>/contents.md: breadcrumb + command-page index table."""
    lines = []
    lines.append("")
    lines.append(f"## [Tcl8.6.18/Tk8.6.18 Documentation](../contents.md) > {sec}")
    lines.append("")
    lines.append(f"{len(pages)} 个命令/页面。")
    lines.append("")
    lines.append("| 页面 | 页面 | 页面 |")
    lines.append("|---|---|---|")
    # 每行 3 列
    row = []
    for p in pages:
        base = p[:-4]  # strip .htm
        name = base
        row.append(f"[{name}]({base}.md)")
        if len(row) == 3:
            lines.append("| " + " | ".join(row) + " |")
            row = []
    if row:
        while len(row) < 3:
            row.append("")
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n"


def mirror_section(sec, force=False):
    url = f"{BASE}/{sec}/contents.htm"
    print(f"[section] {sec}: fetching index {url}")
    data = fetch(url)
    text = data.decode("utf-8", errors="replace")
    if "URL Not Found" in text or "cannot be found" in text:
        print(f"  !! {sec} contents.htm is a 404 page — skipping")
        return 0, 0, []
    pages = collect_pages_in_section(sec, text)
    print(f"  index references {len(pages)} page(s) in {sec}/")
    ok = 0
    fail = 0
    fresh = 0
    failed = []
    for p in pages:
        md_path = os.path.join(OUT, sec, p[:-4] + ".md")
        if not force and os.path.exists(md_path):
            ok += 1
            continue
        fresh += 1
        try:
            d = fetch(f"{BASE}/{sec}/{p}")
        except Exception as e:
            fail += 1
            failed.append(p)
            print(f"    !! {p}: {e}")
            continue
        try:
            md = html_to_md(d)
            save_md(f"{sec}/{p[:-4]}.md", md)
            ok += 1
        except Exception as e:
            fail += 1
            failed.append(p)
            print(f"    !! {p} convert fail: {e}")
    # contents.md（仅当本次新增或强制时写，避免覆盖已有高质量 contents）
    if pages and (fresh > 0 or force):
        ok_set = set(p[:-4] + ".md" for p in pages if os.path.exists(os.path.join(OUT, sec, p[:-4] + ".md")))
        cm = gen_contents_md(sec, pages, ok_set, set(failed))
        save_md(f"{sec}/contents.md", cm)
    print(f"  {sec}: {ok} pages ready, {fail} failed")
    return ok, fail, failed


def gen_top_contents():
    lines = [
        "# Tcl 8.6.18 / Tk 8.6.18 Documentation（本地镜像索引）",
        "",
        "本目录为 `www.tcl-lang.org/man/tcl8.6/` 的本地 Markdown 转档。",
        "",
        "| 分区 | 说明 |",
        "| --- | --- |",
    ]
    meta = {
        "UserCmd": "Tcl/Tk 应用（tclsh / wish 解释器）",
        "TclCmd": "Tcl 命令（tclsh 实现）",
        "TkCmd": "Tk 命令（wish 实现）",
        "ItclCmd": "[incr Tcl] 包命令",
        "SqliteCmd": "SQLite3 包命令",
        "TdbcCmd": "TDBC 包命令",
        "TdbcmysqlCmd": "tdbc::mysql 包命令",
        "TdbcodbcCmd": "tdbc::odbc 包命令",
        "TdbcpostgresCmd": "tdbc::postgres 包命令",
        "TdbcsqliteCmd": "tdbc::sqlite3 包命令",
        "ThreadCmd": "Thread 包命令",
        "TclLib": "Tcl C API",
        "TkLib": "Tk C API",
        "ItclLib": "[incr Tcl] 包 C API",
        "TdbcLib": "TDBC 包 C API",
        "Keywords": "关键词索引",
    }
    for sec in SECTIONS:
        lines.append(f"| [{sec}]({sec}/contents.md) | {meta.get(sec, '')} |")
    lines.append("")
    return "\n".join(lines)


def main():
    os.makedirs(OUT, exist_ok=True)
    force = "--force" in sys.argv
    total_ok = 0
    total_fail = 0
    all_failed = []
    for sec in SECTIONS:
        ok, fail, failed = mirror_section(sec, force=force)
        total_ok += ok
        total_fail += fail
        all_failed += [(sec, f) for f in failed]
    # 根 contents.md 由人工维护（已列出全部 16 分区），此处不覆盖。
    print("\n==== SUMMARY ====")
    print(f"pages ready: {total_ok}")
    print(f"pages failed: {total_fail}")
    if all_failed:
        print("FAILED LIST:")
        for sec, f in all_failed:
            print(f"  {sec}/{f}")
    print(f"output dir: {OUT}")


if __name__ == "__main__":
    main()
