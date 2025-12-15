class Solution {
public:
    int reverse(int x) {
        int reversedNum = 0;

        while (x != 0) {
            int digit = x % 10; // Extract the last digit
            x /= 10; // Remove the last digit

            // Check for 32-bit integer overflow before multiplying by 10
            if (reversedNum > INT_MAX / 10 || (reversedNum == INT_MAX / 10 && digit > 7)) {
                return 0; // Overflow case
            }
            if (reversedNum < INT_MIN / 10 || (reversedNum == INT_MIN / 10 && digit < -8)) {
                return 0; // Underflow case
            }

            reversedNum = reversedNum * 10 + digit; // Append digit
        }

        return reversedNum;
    }
};