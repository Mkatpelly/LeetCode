class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int low = 0, high = n - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            // Check if the current mid position satisfies citations[mid] >= n - mid
            if (citations[mid] >= n - mid) {
                high = mid - 1;  // Move left to find a smaller valid index
            } else {
                low = mid + 1;   // Move right for more citations
            }
        }

        // When the loop finishes, n - low gives the h-index
        return n - low;
    }
}