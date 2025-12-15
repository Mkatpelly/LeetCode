class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length(), n = p.length();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));

        // Base case: empty string matches empty pattern
        dp[0][0] = true;

        // Handling patterns with '*' (matches zero occurrences)
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*' && j >= 2) {
                dp[0][j] = dp[0][j - 2]; // '*' eliminates preceding element
            }
        }

        // DP computation
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == '.' || p[j - 1] == s[i - 1]) {
                    dp[i][j] = dp[i - 1][j - 1]; // Match single character
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 2]; // '*' acts as 0 occurrences
                    if (p[j - 2] == '.' || p[j - 2] == s[i - 1]) {
                        dp[i][j] = dp[i][j] || dp[i - 1][j]; 
                    }
                }
            }
        }

        return dp[m][n];
    }
};