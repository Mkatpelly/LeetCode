class Solution {
    public int minCost(int[][] costs) {
        if (costs == null || costs.length == 0) return 0;
        int n = costs.length;
        // Initialize cumulative costs for each color at the first house
        int red = costs[0][0];
        int blue = costs[0][1];
        int green = costs[0][2];
        
        for (int i = 1; i < n; i++) {
            int newRed = costs[i][0] + Math.min(blue, green);
            int newBlue = costs[i][1] + Math.min(red, green);
            int newGreen = costs[i][2] + Math.min(red, blue);
            // Update cumulative costs for the next iteration
            red = newRed;
            blue = newBlue;
            green = newGreen;
        }
        // Return the minimum among the three color choices for the last house
        return Math.min(red, Math.min(blue, green));
    }
}