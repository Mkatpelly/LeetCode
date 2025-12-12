class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;

        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (int i = 0; i < n; i++) {
            minHeap.offer(new int[]{matrix[i][0], i, 0});
        }
        int count = 0;
        int result = 0;
        while (count < k) {
            int[] current = minHeap.poll();
            result = current[0];
            int row = current[1];
            int col = current[2];

            if (col + 1 < n) {
                minHeap.offer(new int[]{matrix[row][col + 1], row, col + 1});
            }
            count++;
        }

        return result;
    }
}