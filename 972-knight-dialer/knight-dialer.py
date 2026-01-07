class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp[d] = number of ways to end at digit d for current length
        dp = [1] * 10  # length 1

        for _ in range(n - 1):
            ndp = [0] * 10
            ndp[0] = (dp[4] + dp[6]) % MOD
            ndp[1] = (dp[6] + dp[8]) % MOD
            ndp[2] = (dp[7] + dp[9]) % MOD
            ndp[3] = (dp[4] + dp[8]) % MOD
            ndp[4] = (dp[0] + dp[3] + dp[9]) % MOD
            ndp[5] = 0
            ndp[6] = (dp[0] + dp[1] + dp[7]) % MOD
            ndp[7] = (dp[2] + dp[6]) % MOD
            ndp[8] = (dp[1] + dp[3]) % MOD
            ndp[9] = (dp[2] + dp[4]) % MOD
            dp = ndp

        return sum(dp) % MOD