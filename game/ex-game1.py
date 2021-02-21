import tkinter as tk
import random
root = tk.Tk() 
root.geometry("300x300")
canvas = tk.Canvas(root)
oval = ""
rectangle = ""
ball_move_down = True
ra = True
mr = 5
ml = 5
mu = 5
md = 5

def draw_a_ratangle():
    global rectangle
    rectangle = canvas.create_rectangle(100, 120, 200, 140, fill = "red" )
def moveRight(event):
    global rectangle,mr, ml, mu, md, ra
    x1, y1, x2, y2, = canvas.coords(rectangle)
    print(x1, y1, x2, y2)
    canvas.move(rectangle, mr, 0)
    if x2 >  290 :
        print("right")
        mr = 0
        ml = 5
        mu = 5
        md = 5

def moveLeft(event):
    global rectangle,mr, ml, mu, md, ra
    x1, y1, x2, y2 = canvas.coords(rectangle)
    canvas.move(rectangle, - ml, 0)
    print(x1, y1, x2, y2)
    if x1 < 10:
        print("left")
        ml = 0
        mr = 5
        mu = 5
        md = 5

def moveUp(event):
    global rectangle,mr, ml, mu, md, ra
    x1, y1, x2, y2 = canvas.coords(rectangle)
    canvas.move(rectangle, 0, -mu)
    print(x1, y1, x2, y2)
    if y1 < 10:
        print("Up")
        mu = 0
        md = 5
        ml = 5
        mr = 5

def moveDown(event):
    global rectangle,mr, ml, mu, md, ra
    x1, y1, x2, y2 = canvas.coords(rectangle)
    canvas.move(rectangle, 0, md)
    print(x1, y1, x2, y2)
    if y2 > 290:
        print("Down")
        md = 0
        mu = 5
        ml = 5
        mr = 5
draw_a_ratangle()

# call the funtion any the position the user to click

root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)
canvas.pack(expand=True, fill='both')
root.mainloop()