maze = [[0,-1,-1],[0,0,-1],[2,0,0]]
rmax=cmax =   len(maze)
r,c = 3,3

def PossibleSolution(r,c, maze, rmax,cmax):
    if maze[r][c]==2:
        return 'yes'
    res1=res2 = 'no'
    if r+1 < rmax  and c < cmax and maze[r+1][c] !=-1:
        res1= PossibleSolution(r+1,c,maze,rmax,cmax)
    if c+1 < cmax and r< rmax and maze[r][c+1] !=-1:
        res2= PossibleSolution(r,c+1,maze,rmax,cmax)
    if res1 =='yes' or res2 =='yes':
        return 'yes'
    return "no"

def solve_maze(maze,rmax,lmax):
    r, c =0,0
    if maze[r][c]==-1:
        print(maze)
        return "no"
    res1 = PossibleSolution(r+1,c, maze,rmax,lmax)
    res2 = PossibleSolution(r,c+1,maze,rmax,lmax)
    if res1 =="yes" or res2 == "yes":
        return "yes"
    return "no"

res = solve_maze(maze,3,3)
print(res)

    