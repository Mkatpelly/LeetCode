class Solution {
    public void sortColors(int[] nums) {
        
        int low = 0, mid = 0, high = nums.length - 1;

        
        while (mid <= high) {
            if (nums[mid] == 0) {
                
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                // Move the mid pointer
                mid++;
            } else {
                // Swap nums[mid] with nums[high] and move the high pointer
                swap(nums, mid, high);
                high--;
            }
        }
    }

    // Helper method to swap elements in the array
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    
    }
}