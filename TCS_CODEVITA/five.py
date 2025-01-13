def get_next_position(x, y, direction):
    if direction == 'u':
        return x-1, y
    elif direction == 'd':
        return x+1, y
    elif direction == 'l':
        return x, y-1
    else:
        return x, y+1

def check_self_intersection(path):
    # Check if path intersects with itself (excluding start/end points)
    seen = set()
    for pos in path[:-1]:  # Exclude last point since it's same as start
        if pos in seen:
            return True
        seen.add(pos)
    return False

def find_band_path(start_x, start_y, moves, grid_size):
    visited_cells = []
    x, y = start_x, start_y
    visited_cells.append((x, y))
    
    for step in moves:
        x, y = get_next_position(x, y, step)
        if x < 0 or x >= grid_size or y < 0 or y >= grid_size:
            return None
        visited_cells.append((x, y))
    
    return visited_cells

def analyze_band_intersection(first_path, second_path):
    cell_order_first = {pos: idx for idx, pos in enumerate(first_path)}
    cell_order_second = {pos: idx for idx, pos in enumerate(second_path)}
    
    overlapping_cells = set(first_path) & set(second_path)
    
    if not overlapping_cells:
        return 0
    
    for cell1 in overlapping_cells:
        for cell2 in overlapping_cells:
            if cell1 != cell2:
                pos1_a, pos1_b = cell_order_first[cell1], cell_order_first[cell2]
                pos2_a, pos2_b = cell_order_second[cell1], cell_order_second[cell2]
                
                if (pos1_a < pos1_b and pos2_a > pos2_b) or (pos1_a > pos1_b and pos2_a < pos2_b):
                    return "Impossible"
    
    return len(overlapping_cells)

def solve_rubber_bands():
    grid_size = int(input())
    
    # Check size constraint
    if grid_size <= 5 or grid_size >= 25:
        return "Impossible"
    
    x1, y1 = map(int, input().split())
    band1_moves = input().strip()
    x2, y2 = map(int, input().split())
    band2_moves = input().strip()
    
    first_band = find_band_path(x1, y1, band1_moves, grid_size)
    second_band = find_band_path(x2, y2, band2_moves, grid_size)
    
    if not first_band or not second_band:
        return "Impossible"
    
    # Check if bands form closed loops
    if first_band[-1] != (x1, y1) or second_band[-1] != (x2, y2):
        return "Impossible"
    
    # Check for self-intersections
    if check_self_intersection(first_band) or check_self_intersection(second_band):
        return "Impossible"
    
    return analyze_band_intersection(first_band, second_band)

if __name__ == "__main__":
    print(solve_rubber_bands())
