import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)

oval4 = ""
ball_move_down4 = True
move_x4 = 5
move_y4 = 5

# create a oval with the middle position
def draw_a_oval4(x, y, size):
    global oval4
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    oval4 = canvas.create_oval(x1, y1, x2, y2, fill="#ff5e78", outline="#ff5e78")


def moveBall4():
    global oval4, move_x4, move_y4, ball_move_down4
    canvas.after(150, lambda: moveBall4())
    x1, y1, x2, y2 = canvas.coords(oval4)
    canvas.move(oval4, - move_x4, -move_y4)
    if ball_move_down4:
        # if ball at the bottom
        if x1 > 540:
            #ball_move_down = False
            ball_move_down4 = not ball_move_down4
            move_x4 =  5
            move_y4 =  5
            print("have")

        # if ball at the top
    else:
        if x2 < 60:
            # change action
            #ball_move_down = True
            ball_move_down4 = not ball_move_down4
            move_x4 = -5
            move_y4 = -5
            print("not")

draw_a_oval4(580, 580, 20)
moveBall4()

# call the funtion any the position the user to click
canvas.pack(expand=True, fill='both')
root.mainloop()
