"""app.py — 用 pygubu.Builder 运行时加载 demo.ui（声明式 UI + 代码逻辑分离）。

运行：
    pip install -r requirements.txt
    python app.py

关键模式（pygubu 标准用法）：
1. Builder().add_from_file("demo.ui")  —— 解析声明式 UI
2. builder.get_object("mainwindow", root)  —— 取顶层控件（其余控件也可用 id 取）
3. builder.connect_callbacks(self)  —— 把 .ui 里 property command 的 JSON 值
   {"value": "on_add", "cbtype": "simple"} 接到本类同名方法 on_add()
"""
import tkinter as tk
import tkinter.messagebox as mb
import pygubu


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.builder = pygubu.Builder()
        # ① 加载声明式 UI
        self.builder.add_from_file("demo.ui")
        # ② 取出控件（mainwindow 会挂到 root 上）
        self.mainwindow = self.builder.get_object("mainwindow", root)
        self.tree = self.builder.get_object("tree", root)
        self.entry = self.builder.get_object("entry_name", root)
        # ③ 绑定回调：.ui 中 command 属性 JSON 的 value="on_add" -> self.on_add
        self.builder.connect_callbacks(self)

    # —— .ui 里 property command 指向的方法 ——
    def on_add(self):
        text = self.entry.get().strip()
        if not text:
            mb.showwarning("提示", "请输入事项")
            return
        n = len(self.tree.get_children()) + 1
        self.tree.insert("", "end", values=(n, text))
        self.entry.delete(0, "end")

    def on_clear(self):
        for iid in self.tree.get_children():
            self.tree.delete(iid)


def main():
    root = tk.Tk()
    root.withdraw()  # 隐藏根窗口：.ui 的 mainwindow 是 Toplevel，不需要显示 root
    App(root)
    # 用 Toplevel 的事件循环驱动（root 已 withdraw，不会弹出空白 "tk" 窗口）
    root.mainloop()


if __name__ == "__main__":
    main()
