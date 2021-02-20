from tkinter import *

root = Tk()
w = Canvas(root, width=200, height=200)
w.pack()
var = w.create_line(0, 0, 100, 100)
w.coords(var, 0, 0, 400, 25)
root.mainloop()