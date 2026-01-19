class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        m = len(group)

        # dp[g][p]: ways using exactly g members to get profit p (capped at minProfit)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(m):
            members = group[i]
            gain = profit[i]
            # iterate members and profit backwards to ensure 0/1 usage
            for g in range(n, members - 1, -1):
                for p in range(minProfit, -1, -1):
                    newP = min(minProfit, p + gain)
                    dp[g][newP] = (dp[g][newP] + dp[g - members][p]) % MOD

        # sum over all member counts with profit at least minProfit
        res = 0
        for g in range(n + 1):
            res = (res + dp[g][minProfit]) % MOD

        return res