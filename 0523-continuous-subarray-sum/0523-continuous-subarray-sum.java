class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
         Map<Integer, Integer> remainderMap = new HashMap<>();
        remainderMap.put(0, -1); 
        int cumSum = 0;

        for (int i = 0; i < nums.length; i++) {
            cumSum += nums[i];
            int remainder = (cumSum % k + k) % k; 

            if (remainderMap.containsKey(remainder)) {
                if (i - remainderMap.get(remainder) > 1) {
                    return true;
                }
            } else {
                remainderMap.put(remainder, i);
            }
        }

        return false;
    }
}