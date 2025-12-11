class Solution {
    public int shortestDistance(int[][] grid) {
        {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return -1;
        }

        int m = grid.length;
        int n = grid[0].length;

        int[][] distances = new int[m][n];
        int[][] reach = new int[m][n];
        int totalBuildings = 0;

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    totalBuildings++;
                    Queue<int[]> queue = new LinkedList<>();
                    boolean[][] visited = new boolean[m][n];
                    queue.add(new int[] {i, j});
                    int level = 0;

                    while (!queue.isEmpty()) {
                        int size = queue.size();
                        level++;
                        for (int k = 0; k < size; k++) {
                            int[] point = queue.poll();
                            for (int[] dir : directions) {
                                int x = point[0] + dir[0];
                                int y = point[1] + dir[1];
                                if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 0 && !visited[x][y]) {
                                    distances[x][y] += level;
                                    reach[x][y]++;
                                    visited[x][y] = true;
                                    queue.add(new int[] {x, y});
                                }
                            }
                        }
                    }
                }
            }
        }

        int shortest = Integer.MAX_VALUE;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 && reach[i][j] == totalBuildings) {
                    shortest = Math.min(shortest, distances[i][j]);
                }
            }
        }

        return shortest == Integer.MAX_VALUE ? -1 : shortest;

    }
}
}