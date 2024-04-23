import sys

class PrimMST:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v # key with minimum index
        return min_index
    
    def prim_mst(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set) #selecting the next best node which is already not included.
            mst_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] and not mst_set[v] and self.graph[u][v] < key[v]: # if neighbour and not already in mst(which also means dist in graph might be less than the key. Must if traversed for the first time)
                    parent[v] = u
                    key[v] = self.graph[u][v]

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Bridge cost with minimum construction cost")
        print("Road \t\t cost")
        for i in range(1, self.V):
            print(f"{regions[parent[i]]}-{regions[i]} : {self.graph[i][parent[i]]}")


# Example usage

n = int(input("Enter the number of regions you want to connect using bridges"))
print("Enter the name of the regions one by one in order : ")
regions = []
for i in range(n):
    regions.append(input("> "))
print("\n Enter the cost of the bridge construction for each bridge -> ")
print("If bridge is not to be constructed between the two pairings enter 0")
graph = [[0] * n for _ in range(n)]

print(graph)
for i in range(n):
    for j in range(n):
        if i!=j and graph[i][j] == 0:
            cost = int(input(f"{regions[i]}-{regions[j]} >>> "))
            print(cost)
            graph[i][j]= graph[j][i]=cost
            




g = PrimMST(n)
g.graph = graph

g.prim_mst()
