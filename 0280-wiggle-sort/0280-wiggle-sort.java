class Solution {
    public void wiggleSort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            // For odd indices: nums[i] should be >= nums[i - 1]
            // For even indices: nums[i] should be <= nums[i - 1]
            if ((i % 2 == 1 && nums[i] < nums[i - 1]) ||
                (i % 2 == 0 && nums[i] > nums[i - 1])) {
                // Swap to fix the local violation
                int temp = nums[i];
                nums[i] = nums[i - 1];
                nums[i - 1] = temp;
            }
        }
    }
}