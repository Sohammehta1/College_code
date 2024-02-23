import random
import numpy as np

grid = [[0]*4]*4
grid = np.array(grid)


def gen_pos():
    row = random.randint(0,3)
    col = random.randint(0,3)
    return row,col



def start():
    
    while True:
        zero_present = False
        for row in grid:
            if 0  in row:
                zero_present = True
        if not zero_present:
            print("Game Over")
            return
        else:
            while(True):
                row,col = gen_pos()
                if grid[row][col] ==0:
                    grid[row][col] = 2
                    break
            print(grid, '\n')  
            choice = input('> ')
            if choice.lower() == 'u':
                for j in range(4):
                    for k in range(2):
                        for i in range(3):
                            if grid[3-i-1][j] == grid[3-i][j] or (grid[3-i-1][j] ==0):
                                grid[3-i-1][j] += grid[3-i][j]
                                grid[3-i][j] =0
                        
            elif choice.lower() == 'd':
                for j in range(4):
                    for k in range(2):
                        for i in range(3):
                            if grid[i][j] == grid[i+1][j] or (grid[i+1][j] ==0):
                                grid[i+1][j] += grid[i][j]
                                grid[i][j] =0
            elif choice.lower()=='l':
                for i in range(4):
                    for k in range(2):
                        for j in range(3):
                            if grid[i][3-j] == grid[i][3-j-1] or (grid[i][3-j-1] == 0):
                                grid[i][3-j-1] += grid[i][3-j]
                                grid[i][3-j] = 0

            elif choice.lower() =='r':
                for i in range(4):
                    for k in range(2):
                        for j in range(3):
                            if grid[i][j] == grid[i][j+1] or (grid[i][j+1] == 0):
                                grid[i][j+1] += grid[i][j]
                                grid[i][j] = 0
start()