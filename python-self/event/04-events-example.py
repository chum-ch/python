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

def myEventTriggerO(event):
    # print("User has clicked at position : ", event.x, event.y)
    print("The is canvas oval")
canvas = tk.Canvas(frame)
canvas.create_oval(50, 50, 200, 200, fill="red", tags="PNCTarget")
canvas.tag_bind("PNCTarget","<Button-1>",myEventTriggerO)

def myEventTriggerS(event):
    # print("User has clicked at position : ", event.x, event.y)
    print("The is canvas square")
canvas.create_rectangle(100, 50, 250, 200, fill="blue", tags="PNCTargetS")
canvas.tag_bind("PNCTargetS","<Button-1>",myEventTriggerS)

def myEventTriggerR(event):
    # print("User has clicked at position : ", event.x, event.y)
    print("The is canvas ratangle")
canvas.create_rectangle(50, 250, 450, 350, fill="yellow", tags="PNCTargetR")
canvas.tag_bind("PNCTargetR","<Button-1>",myEventTriggerR)

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()