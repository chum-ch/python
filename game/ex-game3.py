import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)
oval = ""
# create a oval with the middle position


def draw_a_oval(x, y, size):
    global oval
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    oval = canvas.create_oval(
        x1, y1, x2, y2, fill="#ff5e78", outline="#ff5e78")

def moveBall():
    global oval
    canvas.after(150, lambda: moveBall())
    canvas.move(oval, -5, 5)


draw_a_oval(580, 20, 20)
moveBall()
# call the funtion any the position the user to click
canvas.pack(expand=True, fill='both')
root.mainloop()
