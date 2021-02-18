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
   # choose a random position
   
   # x = random.randrange(0,10)
   # choose a random size
   # draw the circle
   canvas.create_oval(x1,y1,x2,y2,fill=random.choice(colors))

# call function when click anywhere
root.bind("<Button-1>", drawCircle)

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()