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


def naywhereOval(event):
    # print("User has clicked at postion : ", event.x, event.y)
    # posx = event.x -50
    # posy = event.y - 30
    # # size random
    # randomRadius = random.randrange(60, 200)
    # randomColor = random.choice(color)
    # canvas.create_oval(posx, posy, posx + randomRadius, posy + randomRadius, fill=randomColor)
    posx = event.x
    posy = event.y
    # size random
    randomRadius = random.randrange(60, 200)
    randomColor = random.choice(color)
    canvas.create_oval(posx + randomRadius, posy - randomRadius, posx - randomRadius, posy + randomRadius, fill=randomColor)


color = ["red", "yellow", "blue", "pink"]
canvas = tk.Canvas(frame)
root.bind("<Button-1>", naywhereOval)
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()
