class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # dp[i] = number of ways to decode s[:i]
        dp = [0] * (n + 1)
        dp[0] = 1                     # empty string
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, n + 1):
            # one-digit decode (s[i-1])
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # two-digit decode (s[i-2:i])
            two = int(s[i - 2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
