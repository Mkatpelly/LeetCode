class Solution {
    public int maxProduct(int[] nums) {
        int maxSoFar = nums[0];
        int maxEndingHere = nums[0];
        int minEndingHere = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int tempMax = maxEndingHere;
            maxEndingHere = Math.max(nums[i], Math.max(maxEndingHere * nums[i], minEndingHere * nums[i]));
            minEndingHere = Math.min(nums[i], Math.min(tempMax * nums[i], minEndingHere * nums[i]));
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }
        return maxSoFar;
    }
}