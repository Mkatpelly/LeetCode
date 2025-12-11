class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        PriorityQueue<int[]> capitalHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        PriorityQueue<Integer> profitHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < n; i++) {
            capitalHeap.offer(new int[]{capital[i], profits[i]});
        }
        while (k-- > 0){
            while (!capitalHeap.isEmpty() && capitalHeap.peek()[0] <= w) {
                profitHeap.offer(capitalHeap.poll()[1]);
            }
            if (profitHeap.isEmpty()) break;
            w += profitHeap.poll();
        }
        return w;
    }
}