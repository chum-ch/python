import tkinter as tk
import random

# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("500x500")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Hello PNC")
canvas = tk.Canvas(frame)

# the funtion of the code
# grid
def draw_a_shap(x, y, size):
    global BOARD_SIZE, captainPosition
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    for colIndex in range(BOARD_SIZE):
        for rowIndex in range(BOARD_SIZE):
            if(captainPosition[0] == rowIndex and captainPosition[1] == colIndex):
                canvas.create_rectangle(x1, y1, x2, y2, fill = "red")



BOARD_SIZE = 8
# print the grid with Balook inside
def printBoard(captain):
    global captainPosition
    boardString = ""
    for colIndex in range(BOARD_SIZE):
        for rowIndex in range(BOARD_SIZE):
            if(captainPosition[0] == rowIndex and captainPosition[1] == colIndex):
                boardString += " 1"
            else:
                boardString += " 0"
        boardString += "\n"
    return boardString







# main the code 
# gird the position
for row in range(1, 9):
    for col in range(1,9):
        draw_a_shap(55 * row, 55 * col, 22)

# the action of the positon
captainPosition = [0,0]
print(printBoard(captainPosition))
actionsString = input(">Input action number (R, L, U, D) : ")
# move Right
if(actionsString.upper() == "D"):
    if captainPosition[1] < 9:
        captainPosition[1] += 1
                    # move Left
elif (actionsString.upper() == "U"):
    if captainPosition[1] > 0:
        captainPosition[1] -= 1
                # move Down
elif (actionsString.upper() == "R"):
    if captainPosition[0] < 9:
        captainPosition[0] += 1
            # move Up
elif (actionsString.upper() == "L"):
    if captainPosition[0] > 0:
        captainPosition[0] -= 1

 # pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()