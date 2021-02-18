import tkinter as tk

# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("300x300")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Draw by bro- CHUM")

# HERE YOU CAN START TO DRAW
# canvas is like "svg tag" in HTML, it allows user to draw shapes
canvas = tk.Canvas(frame)
# white eyes
canvas.create_oval(30, 45, 90, 75, outline="#000", fill="#fff")
canvas.create_oval(210, 45, 270, 75, outline="#000", fill="#fff")

# blue eyes
canvas.create_oval(45, 45, 74, 74, fill="#000fff")
canvas.create_oval(225, 45, 254, 74, fill="#000fff")

# red 
canvas.create_oval(135, 135, 165, 165, outline="#000", fill="#ff0000")

# mouse left
canvas.create_rectangle(30, 230, 40, 260, outline="#ff0000", fill="#ff0000")
# mouse bottom
canvas.create_rectangle(30, 260, 260, 270, outline="#ff0000", fill="#ff0000")
# mouse right
canvas.create_rectangle(250, 250, 260, 260, outline="#ff0000", fill="#ff0000")
# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()
