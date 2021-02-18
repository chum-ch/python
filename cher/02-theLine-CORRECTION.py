import tkinter as tk
import random

# Create an empty window
root = tk.Tk()
# Set TK window size to width 600 px and height 200 px
root.geometry("550x200")

canvas = tk.Canvas(root)

randomNumber = random.randrange(0, 10)
for columnIndex in range(0, 10):
    x1 = 10 + (columnIndex * 50)
    x2 = x1 + 50
    fillColor = "blue"
    if randomNumber == columnIndex:
        fillColor = "red"
    canvas.create_oval(x1, 50, x2, 100, fill=fillColor)

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')

# Display all
root.mainloop()
