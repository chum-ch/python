import tkinter as tk


# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# size windows
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
BOARD_SIZE = 10
# print the grid with Balook inside
def printBoard(captainPosition):
    boardString = ""
    for colIndex in range(BOARD_SIZE):
        for rowIndex in range(BOARD_SIZE):
            if(captainPosition[0] == rowIndex and captainPosition[1] == colIndex):
                boardString += " 0"
            else:
                boardString += " 0"
        boardString += "\n"
    return boardString

captainPosition = [0,0]

# Ask player to input action R (right) or L (left) or U (up) or D (down)
def moveRight(event):
    print("right")

def moveLeft(event):
    print("left")

def moveUp(event):
    print("up")
    def moveDown(event):
    print("down")
for i in range(1000):
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
    










canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
root.mainloop()