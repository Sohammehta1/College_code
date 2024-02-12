from heapq import heappush, heappop

class Node:
  def __init__(self, position, parent, g_cost, h_cost):
    self.position = position
    self.parent = parent
    self.g_cost = g_cost  # Cost from start to this node
    self.h_cost = h_cost  # Heuristic estimate of cost to goal
    self.f_cost = g_cost + h_cost  # Total cost estimate

def a_star(start, goal, neighbors, distance, heuristic):
  """
  A* algorithm implementation.

  Args:
    start: Starting position.
    goal: Goal position.
    neighbors: Function that takes a position and returns its neighbors.
    distance: Function that takes two positions and returns the cost of moving between them.
    heuristic: Function that takes a position and returns the estimated cost to goal.

  Returns:
    A list of positions representing the path from start to goal, or None if no path exists.
  """
  open_set = []
  closed_set = set()
  start_node = Node(start, None, 0, heuristic(start, goal))
  heappush(open_set, start_node)

  while open_set:
    current_node = heappop(open_set)
    if current_node.position == goal:
      path = []
      while current_node:
        path.append(current_node.position)
        current_node = current_node.parent
      path.reverse()
      return path

    closed_set.add(current_node.position)

    for neighbor in neighbors(current_node.position):
      if neighbor in closed_set:
        continue
      tentative_g_cost = current_node.g_cost + distance(current_node.position, neighbor)
      new_node = Node(neighbor, current_node, tentative_g_cost, heuristic(neighbor, goal))

      found = False
      for node in open_set:
        if node.position == new_node.position and node.g_cost <= tentative_g_cost:
          found = True
          break
      if not found:
        new_node.parent = current_node
        heappush(open_set, new_node)

  return None

# Example usage (grid-based map):
def neighbors(position):
  x, y = position
  return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def distance(position1, position2):
  x1, y1 = position1
  x2, y2 = position2
  return abs(x1 - x2) + abs(y1 - y2)

def heuristic(position, goal):
  x1, y1 = position
  x2, y2 = goal
  return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance

start = (0, 0)
goal = (4, 4)
path = a_star(start, goal, neighbors, distance, heuristic)

if path:
  print("Path found:", path)
else:
  print("No path found")
