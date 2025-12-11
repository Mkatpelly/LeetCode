class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.length;
        if (n < d) return -1;
        int[][] dp = new int[n + 1][d + 1];
        for (int[] row : dp) Arrays.fill(row, Integer.MAX_VALUE / 2);
        dp[0][0] = 0; // 0 jobs in 0 days costs 0

        for (int days = 1; days <= d; days++) {
            for (int i = days; i <= n; i++) {
                int maxJob = 0;
                // Schedule jobs[j...i-1] on last day
                for (int j = i - 1; j >= days - 1; j--) {
                    maxJob = Math.max(maxJob, jobDifficulty[j]);
                    dp[i][days] = Math.min(dp[i][days], dp[j][days - 1] + maxJob);
                }
            }
        }
        return dp[n][d] >= Integer.MAX_VALUE / 2 ? -1 : dp[n][d];
    }
}