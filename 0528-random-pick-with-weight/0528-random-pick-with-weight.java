class Solution {
    private int[] prefixSum;
    private int totalSum;
    private Random rand;

    public Solution(int[] w) {
        int n = w.length;
        prefixSum = new int[n];
        rand = new Random();
        prefixSum[0] = w[0];
        for (int i = 1; i < n; i++) {
            prefixSum[i] = prefixSum[i - 1] + w[i];
        }
        
        totalSum = prefixSum[n - 1]; 
    }
    
    public int pickIndex() {
        int target = rand.nextInt(totalSum) + 1;
        int left = 0, right = prefixSum.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (prefixSum[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */