class Solution {
    public int minCostII(int[][] costs) {
        if (costs == null || costs.length == 0) return 0;
        int n = costs.length, k = costs[0].length;
        
        int min1 = -1, min2 = -1; // indices of smallest and second smallest costs from previous row
        
        for (int i = 0; i < n; i++) {
            int lastMin1 = min1, lastMin2 = min2;
            min1 = -1; 
            min2 = -1;
            for (int j = 0; j < k; j++) {
                if (i > 0) {
                    // choose the smallest previous cost excluding same color
                    if (j == lastMin1) {
                        costs[i][j] += costs[i - 1][lastMin2];
                    } else {
                        costs[i][j] += costs[i - 1][lastMin1];
                    }
                }
                
                // update smallest and second smallest indices
                if (min1 == -1 || costs[i][j] < costs[i][min1]) {
                    min2 = min1;
                    min1 = j;
                } else if (min2 == -1 || costs[i][j] < costs[i][min2]) {
                    min2 = j;
                }
            }
        }
        return costs[n - 1][min1];
    }
}