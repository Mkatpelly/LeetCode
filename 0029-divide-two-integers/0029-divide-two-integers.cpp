class Solution {
public:
    int divide(int dividend, int divisor) {
        // Handle overflow case
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;

        // Determine the sign of the result
        bool negative = (dividend < 0) ^ (divisor < 0);

        // Convert both numbers to long long and take absolute values
        long long dvd = abs((long long)dividend);
        long long dvs = abs((long long)divisor);
        long long result = 0;

        while (dvd >= dvs) {
            long long temp = dvs, multiple = 1;
            // Double the divisor until it is less than or equal to dividend
            while ((temp << 1) <= dvd) {
                temp <<= 1;
                multiple <<= 1;
            }
            dvd -= temp;
            result += multiple;
        }

        // Apply the sign
        return negative ? -result : result;
    }
};
