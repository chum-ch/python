import tkinter as tk
import random

# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("550x200")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Hello PNC")
canvas = tk.Canvas(frame)

def winFunction(event):
    canvas.create_text(250,140,text="You win!",font=("Purisa", 26))

randomNumber = random.randrange(0,10)
for columnIndex in range(0,10):
    margin = columnIndex * 10
    x1 = 10 + (columnIndex * 50) + margin
    x2 = x1 + 50
    if randomNumber == columnIndex:
        canvas.create_oval(x1, 50, x2, 100, fill="blue", tags="secretCircle")
        canvas.tag_bind("secretCircle", "<Button-1>", winFunction)
    else:
        canvas.create_oval(x1, 50, x2, 100, fill="blue")

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()