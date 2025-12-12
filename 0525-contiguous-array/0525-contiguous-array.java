class Solution {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
         int maxLength = 0;
        int cumulativeSum = 0;

        for (int i = 0; i < nums.length; i++){
             cumulativeSum += (nums[i] == 0) ? -1 : 1;

            if (map.containsKey(cumulativeSum)) {
                maxLength = Math.max(maxLength, i - map.get(cumulativeSum));
            } else {
                map.put(cumulativeSum, i);
            }
        }
        return maxLength;
    }
}