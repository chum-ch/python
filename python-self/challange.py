BOARD_SIZE = 10

# print the grid with Balook inside
def printBoard(captainPosition):
    boardString = ""
    for colIndex in range(BOARD_SIZE):
        for rowIndex in range(BOARD_SIZE):
            if(captainPosition[0] == rowIndex and captainPosition[1] == colIndex):
                boardString += " ★"
            elif (enemies[0] == rowIndex and enemies[1] == colIndex ):
                boardString += " R"
            else:
                boardString += " 0"
        boardString += "\n"
    return boardString

# balook position is [rowIndex, columnIndex]
captainPosition = [0,0]
enemies = eval(input("Please enter positon of enemies!: "))
# call the fuction !
printBoard(captainPosition)

# let the player plays any times
times = True
while times:
    # check the captain be win!
    if (enemies[0] > -1 and enemies[0] < 10) and (enemies[1] > -1 and enemies[1] < 10):
        captainWin = False
        while not captainWin:
            # print board again to see Balook position
            print(printBoard(captainPosition))
            # Ask player to input action R (right) or L (left) or U (up) or D (down)
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
            
            #chack captain win
            if (enemies[0] == captainPosition[0] and enemies[1] == captainPosition[1]):
                print("==============================================================================================")
                print("<<= The captain win! =>>")
                print("==============================================================================================")
                captainWin = True
                times = False
    # The enemies outside the gird !
    else:
        print("==============================================================================================")
        print("NOTE: The position of enemies out of grid! ")
        print("==============================================================================================")
        print("NOTE: It must be stay at the position between 0 to 9.")
        print("==============================================================================================\n\n")
        enemies = eval(input("==> Please enter the position again: "))