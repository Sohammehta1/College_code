import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}  # Key is neighbor name, value is distance
        self.parent = None
        self.g = 0  # Cost from start to current node
        self.h = 0  # Estimated cost from current node to goal (always 0 in this case)
        self.f = 0  # Total cost (g + h)
    def __lt__(self, other):
        return self.f < other.f

def find_path(graph, start_node, goal_node):
    open_list = []  # Nodes to explore, ordered by f-score
    closed_list = set()  # Visited nodes

    start_node.g = 0  # Starting node has no cost from itself
    heapq.heappush(open_list, (start_node.f, start_node))  # Add starting node to open list

    while open_list:
        _, current_node = heapq.heappop(open_list)  # Get node with lowest f-score

        if current_node == goal_node:
            # Found the goal! Backtrack to construct the path
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            path.reverse()
            return path

        closed_list.add(current_node)

        for neighbor_name, _ in current_node.neighbors.items():
            # Skip neighbors already in closed list
            if neighbor_name in closed_list:
                continue

            neighbor = graph[neighbor_name]

            # Calculate tentative g-score for neighbor
            tentative_g = current_node.g + current_node.neighbors[neighbor_name]

            # Check if neighbor already in open list and if new path is better
            if neighbor in (node for _, node in open_list):
                if tentative_g >= neighbor.g:
                    continue
            else:
                # Add neighbor to open list
                neighbor.g = tentative_g
                neighbor.parent = current_node
                # No heuristic in this case (estimated cost always 0)
                neighbor.f = neighbor.g  # Total cost is just g-score
                heapq.heappush(open_list, (neighbor.f, neighbor))

    return None  # No path found

def main():
    # Get number of nodes and create graph
    num_nodes = int(input("Enter the number of nodes: "))
    graph = {}
    for i in range(num_nodes):
        node_name = input("Enter node name: ")
        graph[node_name] = Node(node_name)

    # Get connections and distances
    for node_name, node in graph.items():
        num_connections = int(input(f"Enter the number of connections for {node_name}: "))
        for _ in range(num_connections):
            neighbor_name = input(f"Enter a neighbor for {node_name}: ")
            try:
                distance = float(input(f"Enter the distance to {neighbor_name}: "))
            except ValueError:
                print("Invalid distance. Please enter a number.")
                continue  # Restart input for that connection
            node.neighbors[neighbor_name] = distance

        # No need for estimated distances as user provides all connections and costs

    # Get start and goal nodes
    start_node_name = input("Enter the starting node: ")
    goal_node_name = input("Enter the goal node: ")

    # Set heuristic to 0 since we don't have an estimate
    for node in graph.values():
        node.h = 0

    # Run A* and print path
    path = find_path(graph, graph[start_node_name], graph[goal_node_name])
    if path:
        print("Path found:", path)
        for node_name in path:
            node = graph[node_name]
            print(f"{node_name}: f={node.f}, g={node.g}, h={node.h}")
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
