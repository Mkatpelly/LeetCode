class Solution {
    public int trapRainWater(int[][] heightMap) {
        if (heightMap == null || heightMap.length == 0 || heightMap[0].length == 0) {
            return 0;
        }

        int m = heightMap.length, n = heightMap[0].length;
        boolean[][] visited = new boolean[m][n];
        PriorityQueue<Cell> minHeap = new PriorityQueue<>(Comparator.comparingInt(cell -> cell.height));
        for (int i = 0; i < m; i++) {
            minHeap.offer(new Cell(i, 0, heightMap[i][0]));
            minHeap.offer(new Cell(i, n - 1, heightMap[i][n - 1]));
            visited[i][0] = true;
            visited[i][n - 1] = true;
        }
        for (int j = 1; j < n - 1; j++) {
            minHeap.offer(new Cell(0, j, heightMap[0][j]));
            minHeap.offer(new Cell(m - 1, j, heightMap[m - 1][j]));
            visited[0][j] = true;
            visited[m - 1][j] = true;
        }

        int[] dirs = {-1, 0, 1, 0, -1};
        int waterTrapped = 0;

        while (!minHeap.isEmpty()) {
            Cell cell = minHeap.poll();
            for (int k = 0; k < 4; k++) {
                int newRow = cell.row + dirs[k];
                int newCol = cell.col + dirs[k + 1];
                if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && !visited[newRow][newCol]) {
                    visited[newRow][newCol] = true;
                    waterTrapped += Math.max(0, cell.height - heightMap[newRow][newCol]);
                    minHeap.offer(new Cell(newRow, newCol, Math.max(cell.height, heightMap[newRow][newCol])));
                }
            }
        }

        return waterTrapped;
    }
    private static class Cell {
        int row, col, height;
        Cell(int row, int col, int height) {
            this.row = row;
            this.col = col;
            this.height = height;
        }
    }
}