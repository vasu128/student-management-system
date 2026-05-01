import tkinter as tk
from ui.app import App
from utils.file_handler import initialize_file

if __name__ == "__main__":
    initialize_file()
    root = tk.Tk()
    app = App(root)
    root.mainloop()