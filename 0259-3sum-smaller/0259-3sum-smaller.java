class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int n = nums.length;
        int count = 0;
        
        // Sort the array to use two-pointer technique
        Arrays.sort(nums);
        
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1;
            int right = n - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < target) {
                    // All elements between left and right will form valid triplets with i
                    count += (right - left);
                    left++;
                } else {
                    right--;
                }
            }
        }
        return count;
    }
}