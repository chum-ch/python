import tkinter as tk

root = tk.Tk()
root.geometry("450x500")
canvas = tk.Canvas(root)


def clickAnywhere(event):
    create_a_Oval(event.x, event.y, 25)
    print("x ", event.x, "y ", event.y)


def create_a_Oval(x, y, radius):
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius
    canvas.create_oval(x1, y1, x2, y2, tags="click")


for col in range(1, 8):
    for row in range(1, 8):
        create_a_Oval(row * 55, 55 * col, 25)


canvas.pack(expand=True, fill='both')
root.bind("<Button-1>", clickAnywhere)
root.mainloop()