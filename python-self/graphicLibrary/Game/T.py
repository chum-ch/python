import tkinter as tk
import random

root = tk.Tk()
root.geometry("450x300")
canvas = tk.Canvas(root)
def click(event):
    Oval()
    print(int(event.x / event.x), int(event.y / event.y))
    

def create_a_Oval(x, y,radius):
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius
    canvas.create_oval(x1, y1, x2, y2)
def Oval():
    col = 1
    for x in range(1):
        create_a_Oval(col * 40, 40, 20)
        col += 1
root.bind("<Button - 1>", click)
canvas.pack(expand=True, fill='both')
root.mainloop()
