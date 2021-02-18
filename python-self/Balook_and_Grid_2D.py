
def balookOnCell(CellX, CellY):
    for index in range(len(gird)):
        if (gird[index][0] == CellX) and (gird[index][1] == CellY):
            return True
    return False
gird = eval(input("Enter array 2D and between 0 to 9: "))
boardGird = ""

for row in range(10):
    for col in range(10):
        times = 0
        if balookOnCell(row, col):
            boardGird += "# "
        else:
            boardGird += "0 "
    boardGird += "\n"
print(boardGird)