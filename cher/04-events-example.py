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

def myEventTrigger(event):
    print("User has clicked at position : ", event.x, event.y)

canvas = tk.Canvas(frame)
oval = canvas.create_oval(50, 50, 300, 300, fill="red", tags="PNCTarget")
canvas.tag_bind("PNCTarget","<Button-1>",myEventTrigger)

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()