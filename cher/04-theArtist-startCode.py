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
points = []

def drawCircle(event):
    # In this function : append x and y in array points then draw a small circle at mouse position
    draw_a_oval(event.x, event.y, 4)
    points.append(event.x)
    points.append(event.y)
    print(points)

def drawShape(event):
    # in this function : use "draw_polygon" to draw a shape with the array points. Then empty the points array.
    global points
    canvas.create_polygon(points, fill= random.choice(colors))
    points = []
    print(points)
def draw_a_oval(x, y, size):
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    canvas.create_oval(x1, y1, x2, y2)

root.bind("<Button-1>", drawCircle) #LEFT CLICK
root.bind("<Button-3>", drawShape)  #RIGHT CLICK


# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()