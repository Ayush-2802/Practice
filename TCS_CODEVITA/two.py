import math

def orientation(point1, point2, point3):
    """
    Returns orientation of ordered triplet (point1, point2, point3).
    0 --> Collinear
    1 --> Clockwise
    2 --> Counterclockwise
    """
    val = (point2[1] - point1[1]) * (point3[0] - point2[0]) - \
          (point2[0] - point1[0]) * (point3[1] - point2[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def get_convex_hull(points):
    """
    Implementation of Gift Wrapping algorithm (Jarvis March)
    to find convex hull of a set of points
    """
    num_points = len(points)
    if num_points < 3:
        return points

    # Find leftmost point
    leftmost_idx = min(range(num_points), key=lambda i: points[i][0])
    
    hull_points = []
    current_point = leftmost_idx
    while True:
        hull_points.append(points[current_point])
        next_point = (current_point + 1) % num_points
        
        for point_idx in range(num_points):
            if orientation(points[current_point], points[point_idx], points[next_point]) == 2:
                next_point = point_idx
        
        current_point = next_point
        if current_point == leftmost_idx:
            break
            
    return hull_points

def calculate_perimeter(hull_points):
    """
    Calculate perimeter of the convex hull
    """
    perimeter = 0
    num_vertices = len(hull_points)
    for current_idx in range(num_vertices):
        next_idx = (current_idx + 1) % num_vertices
        x_diff = hull_points[current_idx][0] - hull_points[next_idx][0]
        y_diff = hull_points[current_idx][1] - hull_points[next_idx][1]
        perimeter += math.sqrt(x_diff*x_diff + y_diff*y_diff)
    return round(perimeter)

def main():
    # Read number of points
    num_points = int(input())
    
    # Read points
    point_list = []
    for _ in range(num_points):
        x_coord, y_coord = map(int, input().split())
        point_list.append((x_coord, y_coord))
    
    # Get convex hull
    hull_points = get_convex_hull(point_list)
    
    # Calculate and print perimeter
    perimeter = calculate_perimeter(hull_points)
    print(perimeter)

if __name__ == "__main__":
    main()