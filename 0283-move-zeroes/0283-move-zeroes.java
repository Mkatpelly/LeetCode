class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int nonZeroIndex = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[nonZeroIndex++] = nums[i];
            }
        }
        for (int i = nonZeroIndex; i < n; i++) {
            nums[i] = 0;
        }
    }
}