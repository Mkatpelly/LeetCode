class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        int start = 0, maxLen = 1;

        for (int i = 0; i < s.length(); i++) {
            // Expand around single character center (odd-length palindrome)
            expandFromCenter(s, i, i, start, maxLen);
            // Expand around two-character center (even-length palindrome)
            expandFromCenter(s, i, i + 1, start, maxLen);
        }

        return s.substr(start, maxLen);
    }
private:
    // Function to expand around center and update the longest palindrome
    void expandFromCenter(const string& s, int left, int right, int& start, int& maxLen) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            int len = right - left + 1;
            if (len > maxLen) {
                start = left;
                maxLen = len;
            }
            left--;
            right++;
        }
    }
};