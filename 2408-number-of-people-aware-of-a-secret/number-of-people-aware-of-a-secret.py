class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0  # number of people who can share on current day

        for day in range(2, n + 1):
            # people who now start sharing
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD
            # people who now forget
            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD
            dp[day] = share % MOD

        ans = 0
        # people who haven't forgotten by day n
        start = max(1, n - forget + 1)
        for day in range(start, n + 1):
            ans = (ans + dp[day]) % MOD

        return ans % MOD