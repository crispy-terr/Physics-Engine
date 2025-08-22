import tkinter as tk
from app import App

if __name__ == '__main__':
    part_list = []
    root = tk.Tk()
    root.title("Physics Simulator")
    app = App(root, part_list)
    root.mainloop()