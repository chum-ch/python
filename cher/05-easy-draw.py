import tkinter as tk
import random
root = tk.Tk() 
root.geometry("600x600")
canvas = tk.Canvas(root)

# create a oval with the middle position
def draw_a_oval(x, y, size) :
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    canvas.create_oval(x1, y1, x2, y2, fill=random.choice(colors))

def drawCircle(event):
    draw_a_oval(event.x, event.y, 50)

colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]


# call the funtion any the position the user to click
root.bind("<Button-1>", drawCircle)

canvas.pack(expand=True, fill='both')
root.mainloop()