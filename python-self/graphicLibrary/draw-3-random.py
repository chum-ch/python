import random
import tkinter as tk

# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("600x600")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Draw by bro- CHUM")

# HERE YOU CAN START TO DRAW
# canvas is like "svg tag" in HTML, it allows user to draw shapes
secret = random.randrange(1, 11)
canvas = tk.Canvas(frame)
for x in range(1,11):
    for y in range(1, 11):
        row = x* 50
        col = y* 50
        if x == y:
            canvas.create_oval(row, col, row + 45, col + 45, fill= "#ff0000")
        else:
            canvas.create_oval(row, col, row + 45, col + 45, fill= "#0000ff")

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()