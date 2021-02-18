import tkinter as tk
import random

# Create an empty window
root = tk.Tk()
# Set TK window size to width 600 px and height 200 px
root.geometry("500x300")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame()
# Set the title of the frame
frame.master.title("Hello PNC")


def userWin(event):
    # print("User has clicked at position : ", event.x, event.y)
    canvas.itemconfig(oval, fill="yellow")  # change the color of the canvas
    # canvas.move(oval, 0, -20)   # move the position of the oval
    print(canvas.create_text(250, 200, text="You win!", font=("Purisa", 26)))


canvas = tk.Canvas(frame)
secret = random.randrange(1, 8)
for x in range(1, 8):
    row = x * 50
    if secret == x:
        oval = canvas.create_oval(
            row, 50, row + 45, 95,  fill="#fff000", tags="win")
    else:
        canvas.create_oval(row, 50, row + 45, 95, fill="#000fff")
canvas.tag_bind("win", "<Button-1>", userWin)
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()
