class Solution {
    public int largestIsland(int[][] grid) {
        int n = grid.length;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int islandIndex = 2;
        int[] islandSizes = new int[n * n + 2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    islandSizes[islandIndex] = dfs(grid, i, j, islandIndex, directions);
                    islandIndex++;
                }
            }
        }
        int maxIslandSize = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    Set<Integer> seenIslands = new HashSet<>();
                    int newSize = 1; // Start with the flipped cell
                    for (int[] dir : directions) {
                        int newRow = i + dir[0];
                        int newCol = j + dir[1];
                        if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < n) {
                            int islandIndexAtDir = grid[newRow][newCol];
                            if (islandIndexAtDir > 1 && !seenIslands.contains(islandIndexAtDir)) {
                                newSize += islandSizes[islandIndexAtDir];
                                seenIslands.add(islandIndexAtDir);
                            }
                        }
                    }
                    maxIslandSize = Math.max(maxIslandSize, newSize);
                }
            }
        }
        return maxIslandSize == 0 ? n * n : maxIslandSize;

    }
     private static int dfs(int[][] grid, int row, int col, int islandIndex, int[][] directions) {
        int n = grid.length;
        grid[row][col] = islandIndex;
        int size = 1;
        for (int[] dir : directions) {
            int newRow = row + dir[0];
            int newCol = col + dir[1];
            if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < n && grid[newRow][newCol] == 1) {
                size += dfs(grid, newRow, newCol, islandIndex, directions);
            }
        }
        return size;
    }
}