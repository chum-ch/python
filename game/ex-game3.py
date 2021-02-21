import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)

oval3 = ""
ball_move_down3 = True
move_x3 = 5
move_y3 = 5
# create a oval with the middle position
def draw_a_oval3(x, y, size):
    global oval3
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    oval3 = canvas.create_oval(
        x1, y1, x2, y2, fill="#ff5e78", outline="#ff5e78")

def moveBall3():
    global oval3, ball_move_down3, move_x3, move_y3

    # keep the position of the oval current
    x1, y1, x2, y2 = canvas.coords(oval3)
    canvas.after(150, lambda: moveBall3())
    canvas.move(oval3, - move_x3,  move_y3)

    if ball_move_down3:
        # if ball at the bottom
        if y1 > 540:
            #ball_move_down = False
            ball_move_down3 = not ball_move_down3
            move_x3 = -5
            move_y3 =  -5
            print("have")

        # if ball at the top
    else:
        if y2 < 60:
            # change action
            #ball_move_down = True
            ball_move_down3 = not ball_move_down3
            move_x3 = 5
            move_y3 = 5
            print("not")

draw_a_oval3(580, 20, 20)
moveBall3()
# call the funtion any the position the user to click
canvas.pack(expand=True, fill='both')
root.mainloop()
