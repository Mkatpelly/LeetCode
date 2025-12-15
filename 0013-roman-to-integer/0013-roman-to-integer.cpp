class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> value = {
            {'I', 1}, {'V', 5},   {'X', 10},
            {'L', 50}, {'C', 100},{'D', 500}, {'M', 1000}
        };

        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            int current = value[s[i]];
            int next = (i + 1 < s.length()) ? value[s[i + 1]] : 0;

            if (current < next) {
                total -= current; // Apply subtraction
            } else {
                total += current;
            }
        }

        return total;
    }
};