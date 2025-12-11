class Solution {
    public int minTotalDistance(int[][] grid) {
        List<Integer> rows = new ArrayList<>();
        List<Integer> cols = new ArrayList<>();

        int m = grid.length, n = grid[0].length;

        // Collect row and column indices of all friends (1s)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    rows.add(i);
                }
            }
        }

        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                if (grid[i][j] == 1) {
                    cols.add(j);
                }
            }
        }

        // The median row and column give the optimal meeting point
        int rowMedian = rows.get(rows.size() / 2);
        int colMedian = cols.get(cols.size() / 2);

        return getDistance(rows, rowMedian) + getDistance(cols, colMedian);
    }

    private int getDistance(List<Integer> points, int median) {
        int distance = 0;
        for (int p : points) {
            distance += Math.abs(p - median);
        }
        return distance;
    }
}