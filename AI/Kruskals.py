class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1


def kruskal(graph):
    # Sort edges by weight
    graph.sort(key=lambda x: x[2])
    num_vertices = len(set([edge[0] for edge in graph] + [edge[1] for edge in graph]))
    mst = []
    disjoint_set = DisjointSet(num_vertices)
    for edge in graph:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst.append(edge)
            disjoint_set.union(u, v)
    return mst


# Example usage:
graph = [
    (0, 1, 10), # u,v,weight
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
mst = kruskal(graph)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)