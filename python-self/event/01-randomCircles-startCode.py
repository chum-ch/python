import tkinter as tk
import random

# Create an empty window
root = tk.Tk() 
root.geometry("600x600")
canvas = tk.Canvas(root)
colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet"]

def drawCircle(event):
    randomx = random.randrange(0, 600)
    randomy = random.randrange(0, 600)
    randomSizedifferent = random.randrange(50, 200)
    canvas.create_oval(randomx, randomy, randomx + randomSizedifferent, randomy + randomSizedifferent, fill= random.choice(colors))

# call function when click anywhere
root.bind("<Button-1>", drawCircle)

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')

# Display all
root.mainloop()