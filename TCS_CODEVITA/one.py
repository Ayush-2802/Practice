from collections import deque
from typing import List, Tuple

def read_input() -> Tuple[List[List[str]], List[List[int]], int, Tuple[int, int], Tuple[int, int]]:
    rows, cols = map(int, input().split())
    grid = []
    time_matrix = []
    start = None
    dest = None
    for i in range(rows):
        row = input().split()
        for j in range(len(row)):
            if row[j] == 'S':
                start = (i, j)
            elif row[j] == 'D':
                dest = (i, j)
        grid.append(row)
    for i in range(rows):
        row = list(map(int, input().split()))
        time_matrix.append(row)
        
    initial_strength = int(input())
    return grid, time_matrix, initial_strength, start, dest

def get_shark_strength(cell: str) -> int:
    return 0 if cell in ['S', 'D'] else int(cell)

def find_shortest_path(grid: List[List[str]], time_matrix: List[List[int]], initial_strength: int, 
                      start: Tuple[int, int], dest: Tuple[int, int]) -> Tuple[int, int]:
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Queue stores (row, col, strength, total_time)
    queue = deque([(start[0], start[1], initial_strength, 0)])
    visited = set()
    
    while queue:
        row, col, strength, total_time = queue.popleft()
        
        if (row, col) == dest:
            return total_time, strength
            
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                (new_row, new_col, strength) not in visited):
                
                new_strength = strength - 1  # Basic movement cost
                shark_strength = get_shark_strength(grid[new_row][new_col])
                new_strength -= shark_strength
                new_time = total_time + time_matrix[new_row][new_col]

                if new_strength >= 0:
                    visited.add((new_row, new_col, new_strength))
                    queue.append((new_row, new_col, new_strength, new_time))
    
    return -1, -1

def main():
    grid, time_matrix, initial_strength, start, dest = read_input()
    time, remaining_strength = find_shortest_path(grid, time_matrix, initial_strength, start, dest)
    if time == -1:
        print("Not Possible")
    else:
        print(time, remaining_strength)

if __name__ == "__main__":
    main()