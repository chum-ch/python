import tkinter as tk
import random

# Create an empty window
root = tk.Tk() 
root.geometry("600x600")
canvas = tk.Canvas(root)
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

def drawCircle(event):
    print('narath')
  

# call function when click anywhere
root.bind("<Button-1>", drawCircle)

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')

# Display all
root.mainloop()