import tkinter as tk
import random

root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)
frame = tk.Frame()
frame.master.title("CHUM")

def draw_a_shap(x, y, size):
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    canvas.create_oval(x1, y1, x2, y2, fill=random.choice(colors))


colors = ["red", "orange", "yellow", "green","purple", "brown", "blue", "indigo", "violet"]

canvas.pack(expand=True, fill="both")
root.bind("<Button-1>", draw_a_shap)
root.mainloop()
