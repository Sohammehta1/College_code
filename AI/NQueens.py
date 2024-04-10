import copy
def isValid(position, row,col,queen_cols,n):
    for i in queen_cols:
        if i == col: # if one of the occupied columns = the current col
            return False
    #Check diagonals
    i = row-1
    j = col-1
    while i>=0 and j>=0: #checking for queens diagonally left squares
        if position[i][j] == 'Q':
            return False
        i-=1
        j-=1
    row = row-1 
    col = col+1
    while row>=0 and col <n:
        if position[row][col] == 'Q':
            return False
        row-=1
        col+=1

    return True

def compute_position(last_row:int,position:list[list:chr], possible_solutions:list[list[list:chr]],queen_cols,n):
    curr_row = last_row+1
    if curr_row==n:
        possible_solutions.append(position)
        return
    else:
        for i in range(n):
            new_pos = copy.deepcopy(position)  # Create a deep copy of the board
            new_pos[curr_row][i] = 'Q'
            if isValid(new_pos, curr_row, i,queen_cols,n):
                queen_cols[i]=i
                compute_position(curr_row,new_pos, possible_solutions,queen_cols,n)
                queen_cols[i]=-1
            
def NQueens(n:int)-> list[list:chr]:

    if n > 0 and n <=9:
        initial_board = [['*'] * n for _ in range(n)]  # Forming the board
        possible_solutions=[]
        queen_columns=[-1]*n
        compute_position(-1,initial_board,possible_solutions,queen_columns,n)
        return possible_solutions
    else:return None

ps = NQueens(5)
count = 1
for position in ps:
    print(f"Solution{count} -> ")
    for row in position:
        print(row)
    print('''

''' )
    count += 1
    