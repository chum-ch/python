import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)
# 1
oval1 = ""
move_x_leftT_rightB = 5
move_y_leftT_rightB = 5
# 2
oval2 = ""
move_xleftB_rightT = 5
move_yleftB_rightT = 5
# 3
oval3 = ""
move_x3 = 5
move_y3 = 5
# 4
oval4 = ""
move_x4 = 5
move_y4 = 5
# create a oval with the middle position
# 1
def draw_a_oval(x, y, size):
    global oval1
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    oval1 = canvas.create_oval(
        x1, y1, x2, y2, fill="#6ddccf", outline="#6ddccf")
# 2
def draw_a_oval2(x, y, size):
    global oval2
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    oval2 = canvas.create_oval(
        x1, y1, x2, y2, fill="#f9f871", outline="#f9f871")
# 3
def draw_a_oval3(x, y, size):
    global oval3
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    oval3 = canvas.create_oval(
        x1, y1, x2, y2, fill="#54e346", outline="#54e346")
# 4
def draw_a_oval4(x, y, size):
    global oval4
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    oval4 = canvas.create_oval(x1, y1, x2, y2, fill="#0a043c", outline="#0a043c")

# first ball
def move_ball_leftT_rightB():
    global oval1, move_x_leftT_rightB, move_y_leftT_rightB
    # keep the position of the oval current
    x1, y1, x2, y2 = canvas.coords(oval1)
    # test print the position
    print(x1, y1, x2, y2)
    canvas.after(50, lambda: move_ball_leftT_rightB())
    canvas.move(oval1, move_x_leftT_rightB, move_y_leftT_rightB)
# check condition down or up
   
        # if ball at the bottom
    if y1 > 540:
        move_x_leftT_rightB = - 5
        move_y_leftT_rightB = - 5
        print("bottom")
        # if ball at the top
    
    if y2 < 60:
            move_x_leftT_rightB = 5
            move_y_leftT_rightB = 5
            print("top")

# second ball
def move_ball_leftB_rightT():
    global oval2, move_xleftB_rightT, move_yleftB_rightT
    # keep the position of the oval current
    x1, y1, x2, y2 = canvas.coords(oval2)
    canvas.after(50, lambda: move_ball_leftB_rightT())
    canvas.move(oval2, move_xleftB_rightT, -move_yleftB_rightT)
    # check the condition ball two up and down
    # if ball at the top
    if x1 > 540:
            move_xleftB_rightT = -5
            move_yleftB_rightT =  -5
            print("top")
            
    # if ball at the buttom
    if x2 < 60:
        move_xleftB_rightT = 5
        move_yleftB_rightT = 5
        print("buttom")

# third ball
def moveBall3():
    global oval3, move_x3, move_y3
    # keep the position of the oval current
    x1, y1, x2, y2 = canvas.coords(oval3)
    canvas.after(50, lambda: moveBall3())
    canvas.move(oval3, - move_x3,  move_y3)
    # if ball at the bottom
    if y1 > 540:
        move_x3 = -5
        move_y3 =  -5
        print("have")

    # if ball at the top
    if y2 < 60:
        move_x3 = 5
        move_y3 = 5
        print("not")

# 4
def moveBall4():
    global oval4, move_x4, move_y4
    canvas.after(50, lambda: moveBall4())
    x1, y1, x2, y2 = canvas.coords(oval4)
    canvas.move(oval4, - move_x4, -move_y4)
    # check the condition the ball down or up
    # if ball at the bottom
    if x1 > 540:
        move_x4 =  5
        move_y4 =  5
        print("buttom")

    # if ball at the top
    if x2 < 60:
        move_x4 = -5
        move_y4 = -5
        print("top")

# first ball
draw_a_oval(20, 20, 20)
move_ball_leftT_rightB()

# second ball
draw_a_oval2(20, 580, 20)
move_ball_leftB_rightT()

# third ball
draw_a_oval3(580, 20, 20)
moveBall3()

# fourth ball
draw_a_oval4(580, 580, 20)
moveBall4()

# call the funtion any the position the user to click
canvas.pack(expand=True, fill='both')
root.mainloop()
