import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
# 本应用用相对路径 r'ims.db' 连接数据库，依赖 cwd；统一切到示例目录避免从别处启动时找不到库。
os.chdir(HERE)

import tkinter as tk
import dashboard


def main():
    root = tk.Tk()
    dashboard.IMS(root)
    root.mainloop()


if __name__ == "__main__":
    main()
