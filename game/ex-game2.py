import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)

oval2 = ""
ball_move_down = True
move_xleftB_rightT = 5
move_yleftB_rightT = 5

# create a oval with the middle position
def draw_a_oval(x, y, size):
    global oval2
    x1 = x - size
    y1 = y - size
    x2 = x + size
    oval2 = canvas.create_oval(
        x1, y1, x2, 20, fill="#f9f871", outline="#f9f871")

def move_ball_leftB_rightT():
    global oval2, ball_move_down, move_xleftB_rightT, move_yleftB_rightT

    # keep the position of the oval current
    x1,y1, x2, y2 = canvas.coords(oval2)
    canvas.after(50, lambda: move_ball_leftB_rightT())
    canvas.move(oval2, move_xleftB_rightT, -move_yleftB_rightT)

    if ball_move_down:
        # if ball at the bottom
        if x1 > 100:
            #ball_move_down = False
            ball_move_down = not ball_move_down
            move_xleftB_rightT = -5
            move_yleftB_rightT =  -5
            print("have")

        # if ball at the top
    else:
        if x2 < 60:
            # change action
            #ball_move_down = True
            ball_move_down = not ball_move_down
            move_xleftB_rightT = 5
            move_yleftB_rightT = 5
            print("not")

# second ball
draw_a_oval(20, 580, 20)
move_ball_leftB_rightT()

# call the funtion any the position the user to click
canvas.pack(expand=True, fill='both')
root.mainloop()
