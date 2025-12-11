class Solution {
    public List<List<Integer>> findMissingRanges(int[] nums, int lower, int upper) {
        List<List<Integer>> result = new ArrayList<>();
        int prev = lower - 1;

        for (int i = 0; i <= nums.length; i++) {
            int curr = (i == nums.length) ? upper + 1 : nums[i];

            if (prev + 1 <= curr - 1) {
                result.add(createRange(prev + 1, curr - 1));
            }

            prev = curr;
        }

        return result;

    }
    private static List<Integer> createRange(int start, int end) {
        List<Integer> range = new ArrayList<>();
        range.add(start);
        range.add(end);
        return range;
    }
}