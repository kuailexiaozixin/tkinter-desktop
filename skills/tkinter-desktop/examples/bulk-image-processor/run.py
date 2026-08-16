import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import tkinter as tk
from image_processor_app import ImageProcessorApp


def main():
    root = tk.Tk()
    ImageProcessorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
