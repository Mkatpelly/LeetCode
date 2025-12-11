class Solution {
    public long maxRunTime(int n, int[] batteries) {
        long sum = 0;
        for (int b : batteries) sum += b;

        long left = 0;
        long right = sum / n; // upper bound on possible minutes

        while (left < right) {
            long mid = (left + right + 1) / 2; // candidate minutes

            long usable = 0;
            for (int b : batteries) {
                usable += Math.min((long) b, mid);
                if (usable >= mid * n) break; // early stop
            }

            if (usable >= mid * n) {
                left = mid;      // feasible, try longer time
            } else {
                right = mid - 1; // not feasible, try shorter time
            }
        }

        return left;
    }
}