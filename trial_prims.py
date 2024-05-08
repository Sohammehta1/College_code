import sys 

class PrimsMST:
    def __init__(self,n, graph):
        self.vertices=n
        self.graph = graph

    def printMST(self,parent_list):
        print("Bridge cost with minimum construction cost")
        print("Road \t\t cost")
        for v in range(self.vertices):
            print(f"{regions[parent_list[v]]}-{regions[v]}: {self.graph[v][parent_list[v]]}")
            

    def minKey(self,cost,mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.vertices):
            if cost[v] < min_val and not mst_set[v]:
                min_val=cost[v]
                min_index = v
        return min_index
    
    def prims(self):
        n = self.vertices
        parent = [-1]*n
        cost = [sys.maxsize]*n
        mst_set =[False]*n
        cost[0]=0

        for v in range(n):
            u = self.minKey(cost,mst_set)
            mst_set[u] = True

            for v in range(n):
                if graph[u][v]!=0 and graph[u][v] < cost[v] and not mst_set[v]:
                    parent[v]=u
                    cost[v]= self.graph[u][v]
        self.printMST(parent)


n = int(input("Enter the number of regions you want to connect using bridges"))
print("Enter the name of the regions one by one in order : ")
regions = []
for i in range(n):
    regions.append(input("> "))
print("\n Enter the cost of the bridge construction for each bridge -> ")
print("If bridge is not to be constructed between the two pairings enter 0")
graph = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j and graph[i][j]==0:
            cost = int(input(f"{regions[i]}-{regions[j]} >>> "))
            graph[i][j]=graph[j][i]=cost

pm = PrimsMST(n, graph)
pm.prims()
