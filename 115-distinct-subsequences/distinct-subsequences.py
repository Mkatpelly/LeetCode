class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)

        # dp[i][j] = number of ways to form t[:j] from s[:i]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Empty t can be formed from any prefix of s in exactly one way
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Always can skip current char in s
                dp[i][j] = dp[i - 1][j]

                if s[i - 1] == t[j - 1]:
                    # Optionally use this matching character
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[m][n]