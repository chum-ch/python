# IMPORTS
import tkinter as tk

# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SIZE = 50
MARGIN = 120
# VARIABLES
grid = [0,0,1,0,0,0,0]

# FUNCTIONS
# move the right
def moveRight(event):
    print("right")
    global grid
    index_of_one = 0
    for index_grid in range(len(grid)):
        if grid[index_grid] == 1:
            index_of_one = index_grid
            grid[index_grid] = 0
    if index_of_one < len(grid) -1:
        index_of_one += 1
    grid[index_of_one] = 1
    arrayToDrawing()
    print(grid)

# move the left
def moveLeft(event):
    print("left")
    global grid
    index_of_one = 0
    for index_grid in range(len(grid)):
        if grid[index_grid] == 1:
            index_of_one = index_grid
            grid[index_grid] = 0
    if index_of_one > 0:
        index_of_one -= 1
    grid[index_of_one] = 1
    arrayToDrawing()
    print(grid)
def arrayToDrawing():
    global grid
    for index in range (len(grid)):
        x1=SIZE * index + MARGIN
        y1=SIZE
        x2=SIZE + x1
        y2=SIZE + y1

# draw a line with white and black squares using the global array
        if grid[index] == 0:
            color="white"
        else:
            color="black"
        canvas.create_rectangle(x1,y1,x2,y2,fill=color)


root = tk.Tk()
root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))

canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")

arrayToDrawing()
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
root.mainloop()