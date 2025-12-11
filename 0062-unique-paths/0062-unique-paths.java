class Solution {
    public int uniquePaths(int m, int n) {
        long result = 1;
        int totalSteps = m + n - 2;
        int minSteps = Math.min(m - 1, n - 1);
        for (int i = 0; i < minSteps; i++) {
            result = result * (totalSteps - i) / (i + 1);
        }
        return (int) result;
    }
}