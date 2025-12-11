class Solution {
    public String largestNumber(int[] nums) {
        // Convert the integers to strings for custom sorting
        String[] numStrings = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            numStrings[i] = String.valueOf(nums[i]);
        }

        // Sort the strings using a custom comparator
        Arrays.sort(numStrings, (a, b) -> (b + a).compareTo(a + b));

        // If the largest number is "0", the entire number is "0"
        if (numStrings[0].equals("0")) {
            return "0";
        }

        // Build the largest number by concatenating the sorted strings
        StringBuilder result = new StringBuilder();
        for (String num : numStrings) {
            result.append(num);
        }

        return result.toString();
    }
}