class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> cumSumFreq = new HashMap<>();
        cumSumFreq.put(0, 1); 
        int cumSum = 0;
        int count = 0;

        for (int num : nums) {
            cumSum += num;
            if (cumSumFreq.containsKey(cumSum - k)) {
                count += cumSumFreq.get(cumSum - k);
            }
            cumSumFreq.put(cumSum, cumSumFreq.getOrDefault(cumSum, 0) + 1);
        }

        return count;
    }
}