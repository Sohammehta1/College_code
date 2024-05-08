import copy

class Node:
    def __init__(self,data,level,fval):
        self.data = data
        self.level = level
        self.fval = fval
    
    def find(self,puz,x):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j]==x:
                    return i,j
                
    def shuffle(self,puz,x1,y1,x2,y2):
        if x2 >=0 and x2 <len(self.data) and y2>=0 and y2 <len(self.data):
            temp_puz = copy.deepcopy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2]= '_'
            temp_puz[x1][y1]=temp
            return temp_puz
        else:
            return None

    def generate_children(self):
        x,y=self.find(self.data,'_')
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                childNode = Node(child,self.level+1,0)
                children.append(childNode)
        return children
    
class Puzzle:
    def __init__(self,size):
        self.n  = size
        self.open =[]
        self.closed=[]
    
    def accept(self):
        puz = []
        for i in range(self.n):
            row = input("> ").split(" ")
            puz.append(row)
        return puz
    def f(self,curr_state,goal):
        return self.h(curr_state.data,goal)+curr_state.level
    
    def h(self,curr_state,goal):
        diff = 0
        for i in range(self.n):
            for j in range(self.n):
                if curr_state[i][j]!=goal[i][j]:
                    diff += 1
        return diff
    
    def Process(self):
        print("Enter initial puzzle : ")
        start = self.accept()
        print("\nEnter goal state : ")
        goal = self.accept()

        start = Node(start,0,0)
        start.fval = self.f(start,goal)

        #Putting starting position on the open list
        self.open.append(start)
        print("\n\n")
        while(True):
            if len(self.open)==0:
                print("No solution exists")
                return 
            curr = self.open[0]
            print("||")
            print("\/\n")
            for i in curr.data:
                for j in i:
                    print(j, end=" ")
                print("")
            if self.h(curr.data,goal)==0: # Goal state is reached
                break
            for i in curr.generate_children():
                i.fval = self.f(curr,goal)
                if i not in self.open and i not in self.closed:
                    self.open.append(i)
            self.closed.append(curr)
            del self.open[0] 

            self.open.sort(key=lambda x:x.fval,reverse=False)

puz = Puzzle(2)
puz.Process()