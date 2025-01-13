import math
from collections import defaultdict, deque

def check_collision(v_x, v_y, v_r, b_x, b_y, b_r):
    # Calculate distance between centers
    dist = math.sqrt((v_x - b_x)**2 + (v_y - b_y)**2)
    return dist < (v_r + b_r)

def find_closest_building(x, y, buildings):
    min_dist = float('inf')
    closest_idx = -1
    
    for idx, (b_x, b_y, b_r) in enumerate(buildings):
        dist = math.sqrt((x - b_x)**2 + (y - b_y)**2)
        if dist < min_dist:
            min_dist = dist
            closest_idx = idx
    
    return closest_idx

def solve(start_x, start_y, end_x, end_y, vehicle_radius, buildings, tax_lines):
    # Create adjacency list for the graph
    graph = defaultdict(list)
    for a, b in tax_lines:
        graph[a-1].append(b-1)  # Convert to 0-based indexing
        graph[b-1].append(a-1)
    
    # Find closest buildings to start and end points
    start_building = find_closest_building(start_x, start_y, buildings)
    end_building = find_closest_building(end_x, end_y, buildings)
    
    # Check if valid buildings were found
    if start_building == -1 or end_building == -1:
        return "Impossible"
    
    # Check if vehicle collides with any building
    for b_x, b_y, b_r in buildings:
        if check_collision(start_x, start_y, vehicle_radius, b_x, b_y, b_r):
            return "Impossible"
    
    # BFS to find shortest path
    visited = set()
    queue = deque([(start_building, 0)])  # (node, distance)
    visited.add(start_building)
    
    while queue:
        current, dist = queue.popleft()
        
        if current == end_building:
            return dist
        
        for next_building in graph[current]:
            if next_building not in visited:
                # Check for collision with vehicle
                collision = False
                b_x, b_y, b_r = buildings[next_building]
                if check_collision(start_x, start_y, vehicle_radius, b_x, b_y, b_r):
                    collision = True
                
                if not collision:
                    visited.add(next_building)
                    queue.append((next_building, dist + 1))
    
    return "Impossible"

# Example usage:
# buildings = [(x, y, r), ...]  # List of tuples containing building coordinates and radius
# tax_lines = [(a, b), ...]     # List of tuples containing building pairs connected by tax lines
# Read input
S = int(input())
start_x, start_y, vehicle_radius = map(int, input().split())
end_x, end_y = map(int, input().split())

N = int(input())
buildings = []
for _ in range(N):
    x, y, r = map(int, input().split())
    buildings.append((x, y, r))

T = int(input())
tax_lines = []
for _ in range(T):
    a, b = map(int, input().split())
    tax_lines.append((a, b))

# Solve and print result
result = solve(start_x, start_y, end_x, end_y, vehicle_radius, buildings, tax_lines)
print(result)