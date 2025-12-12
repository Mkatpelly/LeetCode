class Solution {
    public int maximumSwap(int num) {
        char[] digits = Integer.toString(num).toCharArray();
        int n = digits.length;
        int[] maxRight = new int[n];
        maxRight[n - 1] = n - 1;
        for (int i = n - 2; i >= 0; i--) {
            if (digits[i] > digits[maxRight[i + 1]]) {
                maxRight[i] = i;
            } else {
                maxRight[i] = maxRight[i + 1];
            }
        }
        for (int i = 0; i < n; i++) {
            if (digits[i] != digits[maxRight[i]]) {
                char temp = digits[i];
                digits[i] = digits[maxRight[i]];
                digits[maxRight[i]] = temp;
                break;
            }
        }
        return Integer.parseInt(new String(digits));
    }
}