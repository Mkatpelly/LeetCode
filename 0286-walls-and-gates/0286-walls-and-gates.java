class Solution {
    public void wallsAndGates(int[][] rooms) {
        if (rooms == null || rooms.length == 0 || rooms[0].length == 0) return;

        int m = rooms.length, n = rooms[0].length;
        Queue<int[]> queue = new LinkedList<>();

        // Step 1: Add all gates (cells with value 0) to the BFS queue
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        // Step 2: Multi-source BFS from all gates simultaneously
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0], col = cell[1];

            for (int[] dir : directions) {
                int r = row + dir[0];
                int c = col + dir[1];

                // Skip out-of-bounds and non-empty rooms
                if (r < 0 || c < 0 || r >= m || c >= n || rooms[r][c] != Integer.MAX_VALUE) {
                    continue;
                }

                // Update distance and add to queue
                rooms[r][c] = rooms[row][col] + 1;
                queue.offer(new int[]{r, c});
            }
        }
    }
}