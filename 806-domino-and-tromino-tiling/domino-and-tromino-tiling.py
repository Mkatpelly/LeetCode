class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        dp0, dp1, dp2 = 1, 1, 2  # dp[0], dp[1], dp[2]

        # we already know dp[3] = 5
        dp3 = (2 * dp2 + dp0) % MOD  # 2*2 + 1 = 5
        if n == 3:
            return dp3

        # shift window: dp[i-3], dp[i-2], dp[i-1]
        a, b, c = dp1, dp2, dp3  # dp[1], dp[2], dp[3]

        for i in range(4, n + 1):
            d = (2 * c + a) % MOD   # dp[i] = 2*dp[i-1] + dp[i-3]
            a, b, c = b, c, d

        return c