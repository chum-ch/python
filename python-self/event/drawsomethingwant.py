import tkinter as tk
import random

# Create an empty window
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)
colors = ["red", "orange", "yellow", "green","purple", "brown", "blue", "indigo", "violet"]
def outOval(event):
    draw_a_Oval(event.x, event.y, 20)


def draw_a_Oval(x, y, radius):
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius
    canvas.create_oval(x1, y1, x2, y2, fill= random.choice(colors))






# call function when click anywhere
#root.bind("<Button-1>", drawCircle)

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
root.bind("<Button-1>", outOval)
# Display all
root.mainloop()
