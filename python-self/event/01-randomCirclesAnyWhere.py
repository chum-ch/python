import tkinter as tk
import random

# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("600x600")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Hello PNC")
canvas = tk.Canvas(frame)
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

def drawCircle(event):
    x1 = random.randrange(-100,600)
    y1 = random.randrange(-100,600)
    radius = random.randrange(50,200)
    color = random.choice(colors)
    canvas.create_oval(x1, y1, x1+radius,y1+radius, fill=color)

# call function when click anywhere
root.bind("<Button-1>", drawCircle)

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()