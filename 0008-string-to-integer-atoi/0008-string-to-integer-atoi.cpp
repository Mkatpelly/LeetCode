class Solution {
public:
    int myAtoi(string s) {
        int i = 0, n = s.length();
        int sign = 1;  // Default sign is positive
        long result = 0; // Using long to detect overflow

        // Step 1: Ignore leading whitespace
        while (i < n && s[i] == ' ') i++;

        // Step 2: Handle optional '+' or '-'
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }

        // Step 3: Convert digits into an integer
        while (i < n && isdigit(s[i])) {
            result = result * 10 + (s[i] - '0');
            
            // Step 4: Handle overflow cases
            if (sign * result > INT_MAX) return INT_MAX;
            if (sign * result < INT_MIN) return INT_MIN;

            i++;
        }

        return sign * result; // Return final result with sign
    }
};