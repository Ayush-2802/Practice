from collections import deque
from typing import List, Tuple
from heapq import heappush, heappop

def read_input() -> Tuple[List[List[str]], List[List[int]], int, Tuple[int, int], Tuple[int, int]]:
    grid_height, grid_width = map(int, input().split())
    ocean_grid = []
    travel_time = []
    start_position = None
    destination = None
    
    # Pre-allocate lists for better memory efficiency
    ocean_grid = [None] * grid_height
    travel_time = [None] * grid_height
    
    for row_idx in range(grid_height):
        current_row = input().split()
        for col_idx in range(grid_width):  # Use grid_width instead of len()
            if current_row[col_idx] == 'S':
                start_position = (row_idx, col_idx)
            elif current_row[col_idx] == 'D':
                destination = (row_idx, col_idx)
        ocean_grid[row_idx] = current_row
        
    for row_idx in range(grid_height):
        travel_time[row_idx] = list(map(int, input().split()))
    
    return ocean_grid, travel_time, int(input()), start_position, destination

def find_shortest_path(ocean_grid: List[List[str]], travel_time: List[List[int]], diver_strength: int, 
                      start_position: Tuple[int, int], destination: Tuple[int, int]) -> Tuple[int, int]:
    grid_height, grid_width = len(ocean_grid), len(ocean_grid[0])
    possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Use priority queue for optimal path finding
    pq = [(0, diver_strength, start_position[0], start_position[1])]
    explored_positions = {start_position: diver_strength}
    
    while pq:
        elapsed_time, remaining_strength, current_row, current_col = heappop(pq)
        
        if (current_row, current_col) == destination:
            return elapsed_time, remaining_strength
            
        for move_row, move_col in possible_moves:
            next_row, next_col = current_row + move_row, current_col + move_col
            if 0 <= next_row < grid_height and 0 <= next_col < grid_width:
                cell = ocean_grid[next_row][next_col]
                shark_power = 0 if cell in 'SD' else int(cell)
                updated_strength = remaining_strength - 1 - shark_power
                
                if updated_strength >= 0:
                    current_best = explored_positions.get((next_row, next_col), -1)
                    if updated_strength > current_best:
                        updated_time = elapsed_time + travel_time[next_row][next_col]
                        explored_positions[(next_row, next_col)] = updated_strength
                        heappush(pq, (updated_time, updated_strength, next_row, next_col))
    
    return -1, -1

def main():
    result = find_shortest_path(*read_input())
    print("Not Possible" if result[0] == -1 else f"{result[0]} {result[1]}")

if __name__ == "__main__":
    main()
