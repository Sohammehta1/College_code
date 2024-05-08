
def dfs(start_node,adj_list : dict,n:int) :

    def visit_neighbours(vnodes,curr,parent_node):
        vnodes[curr] = True
        for neighbour in adj_list[curr]:
            if visited_nodes[neighbour] != True:
                if visit_neighbours(visited_nodes,neighbour,curr):
                    return True
            elif neighbour !=parent_node:
                return True
    visited_nodes = {}
    for node in adj_list.keys():
        visited_nodes[node] = False
    
    return visit_neighbours(visited_nodes,start_node,start_node)


graph ={
    0:[1,2,3],
    1:[0,3],
    2:[0],
    3:[0,1,4,5],
    4:[3,5],
    5:[3,4]
}

graph2 ={
    0:[1,2,3],
    1:[0],
    2:[0],
    3:[0]
}

if dfs(2,graph2,4):
    print("Cycle is present")
else:
    print("Cycle is absent")



    
            