    import java.util.*;

    class Point {
        int row, col, strength, time;
        Point(int row, int col, int strength, int time) {
            this.row = row;
            this.col = col;
            this.strength = strength;
            this.time = time;
        }
    }

    public class Main {
        static class InputData {
            String[][] oceanGrid;
            int[][] travelTime;
            int diverStrength;
            Point start, destination;
            
            InputData(String[][] grid, int[][] time, int strength, Point start, Point dest) {
                this.oceanGrid = grid;
                this.travelTime = time;
                this.diverStrength = strength;
                this.start = start;
                this.destination = dest;
            }
        }

        static InputData readInput() {
            Scanner scanner = new Scanner(System.in);
            int height = scanner.nextInt();
            int width = scanner.nextInt();
            scanner.nextLine();

            String[][] oceanGrid = new String[height][width];
            int[][] travelTime = new int[height][width];
            Point start = null, destination = null;

            for (int i = 0; i < height; i++) {
                String[] row = scanner.nextLine().split(" ");
                for (int j = 0; j < width; j++) {
                    oceanGrid[i][j] = row[j];
                    if (row[j].equals("S")) start = new Point(i, j, 0, 0);
                    if (row[j].equals("D")) destination = new Point(i, j, 0, 0);
                }
            }

            for (int i = 0; i < height; i++) {
                for (int j = 0; j < width; j++) {
                    travelTime[i][j] = scanner.nextInt();
                }
            }

            int diverStrength = scanner.nextInt();
            return new InputData(oceanGrid, travelTime, diverStrength, start, destination);
        }

        static int getSharkStrength(String position) {
            return position.equals("S") || position.equals("D") ? 0 : Integer.parseInt(position);
        }

        static int[] findShortestPath(InputData input) {
            int height = input.oceanGrid.length;
            int width = input.oceanGrid[0].length;
            int[][] dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};
            
            Queue<Point> queue = new LinkedList<>();
            Map<String, Integer> explored = new HashMap<>();
            
            queue.offer(new Point(input.start.row, input.start.col, input.diverStrength, 0));
            explored.put(input.start.row + "," + input.start.col, input.diverStrength);

            while (!queue.isEmpty()) {
                Point current = queue.poll();
                
                if (current.row == input.destination.row && current.col == input.destination.col) {
                    return new int[]{current.time, current.strength};
                }

                for (int[] dir : dirs) {
                    int nextRow = current.row + dir[0];
                    int nextCol = current.col + dir[1];
                    
                    if (nextRow >= 0 && nextRow < height && nextCol >= 0 && nextCol < width) {
                        int updatedStrength = current.strength - 1 - getSharkStrength(input.oceanGrid[nextRow][nextCol]);
                        
                        if (updatedStrength >= 0) {
                            String key = nextRow + "," + nextCol;
                            int currentBest = explored.getOrDefault(key, -1);
                            
                            if (updatedStrength > currentBest) {
                                int updatedTime = current.time + input.travelTime[nextRow][nextCol];
                                explored.put(key, updatedStrength);
                                queue.offer(new Point(nextRow, nextCol, updatedStrength, updatedTime));
                            }
                        }
                    }
                }
            }
            return new int[]{-1, -1};
        }

        public static void main(String[] args) {
            InputData input = readInput();
            int[] result = findShortestPath(input);
            
            if (result[0] == -1) {
                System.out.println("Not Possible");
            } else {
                System.out.println(result[0] + " " + result[1]);
            }
        }
    }