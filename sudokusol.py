sizes = {6:[2,3],9:[3,3],15:[3,5]}
def isValid(grid,x,y,v,size):
    rowCheck = all([v != grid[x][j] for j in range(size)])
    if rowCheck:
        colCheck = all([v != grid[j][y] for j in range(size)])
        if colCheck:
            startX = sizes[size][0] * (x//sizes[size][0])
            startY = sizes[size][1] * (y//sizes[size][1])
            for i in range(startX,startX + sizes[size][0]):
                for j in range(startY,startY + sizes[size][1]):
                    if grid[i][j] == v:
                        return False
            return True
    return False

def nextCell(grid,x,y,size):
    for i in range(x,size):
        for j in range(y,size):
            if grid[i][j] == 0:
                return i,j
    for i in range(0,size):
        for j in range(0,size):
            if grid[i][j] ==0:
                return i,j
    return -1,-1

def sudoku(grid,x,y,size):
    x,y = nextCell(grid,x,y,size)
    if x == -1:
        return True
    for value in range(1,size+1):
        if isValid(grid,x,y,value,size):
            grid[x][y] = value
            if sudoku(grid,x,y,size):
                return True

            grid[x][y] = 0
    return False
