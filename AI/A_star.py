import heapq

class Node:
    h_n = {
        'Katraj': 10,
        'Bibvewadi': 8,
        'Sahakarnagar': 7,
        'Parvati': 5,
        'Lokmanyanagar': 3,
        'Sinhgad_rd': 2,
        'Kothrud': 0
    }
    
    def __init__(self, location, parent=None, cost=0, fn=0):
        self.location = location
        self.parent = parent
        self.cost = cost
        self.fn = fn

    def __lt__(self, other):
        return (self.fn < other.fn)

def A_star(start, goal, cost_list):
    start_node = Node(start)
    frontier = []
    heapq.heappush(frontier, start_node)
    explored = set()

    while frontier:
        current_node = heapq.heappop(frontier)

        if current_node.location == goal:
            path = []
            final_cost = current_node.cost
            while current_node.parent:
                path.append((current_node.location, current_node.fn))
                current_node = current_node.parent
            path.append((start, Node.h_n[start]))
            path.reverse()
            return path, final_cost

        explored.add(current_node.location)

        for neighbor, cost in cost_list[current_node.location].items():
            new_cost = current_node.cost + cost
            new_node = Node(neighbor, current_node, new_cost, new_cost + Node.h_n[neighbor])
            if neighbor not in explored:
                heapq.heappush(frontier, new_node)
            elif new_cost < current_node.cost:  # Backtrack if a better path to the neighbor is found
                current_node.parent = new_node
                current_node.cost = new_cost
                current_node.fn = new_cost + Node.h_n[current_node.location]

    return None, None

start_location = 'Katraj'
goal_location = 'Kothrud'

cost_list = {
    'Katraj': {'Bibvewadi': 3.5, 'Sahakarnagar': 5},
    'Bibvewadi': {'Katraj': 3.5, 'Sahakarnagar': 2, 'Lokmanyanagar': 6, 'Sinhgad_rd': 5},
    'Sahakarnagar': {'Katraj': 5, 'Bibvewadi': 2, 'Parvati': 1.5, 'Lokmanyanagar': 3, 'Sinhgad_rd': 2.5},
    'Parvati': {'Lokmanyanagar': 2},
    'Lokmanyanagar': {'Bibvewadi': 6, 'Sahakarnagar': 3, 'Parvati': 2, 'Sinhgad_rd': 1, 'Kothrud': 3},
    'Sinhgad_rd': {'Bibvewadi': 5, 'Sahakarnagar': 2.5, 'Lokmanyanagar': 1, 'Kothrud': 2.5},
    'Kothrud': {'Lokmanyanagar': 3, 'Sinhgad_rd': 2.5}
}

path, final_cost = A_star(start_location, goal_location, cost_list)

if path:
    print("Path:", path)
    print("Final Cost:", final_cost)
else:
    print("No path found")
