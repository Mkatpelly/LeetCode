class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> charIndex; // Map to store the last index of characters
        int maxLength = 0;
        int left = 0; // Left pointer for sliding window

        for (int right = 0; right < s.length(); right++) {
            if (charIndex.find(s[right]) != charIndex.end()) {
                // Move left pointer to avoid repeating character
                left = max(left, charIndex[s[right]] + 1);
            }
            // Update last seen index of current character
            charIndex[s[right]] = right;

            // Calculate max length of substring
            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};