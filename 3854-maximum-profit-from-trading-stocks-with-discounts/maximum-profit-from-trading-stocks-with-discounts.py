class Solution(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """
        present = [0] + present  # 1-based
        future = [0] + future

        children = defaultdict(list)
        for u, v in hierarchy:
            children[u].append(v)

        NEG_INF = -10**18

        # dp[u][parentBuys] -> list of size budget+1
        # parentBuys index: 0 = False, 1 = True
        memo = {}

        def dfs(u, parentBuys):
            key = (u, parentBuys)
            if key in memo:
                return memo[key]

            # Case: u does NOT buy, children see parentBuys = False
            dpSkip = [NEG_INF] * (budget + 1)
            dpSkip[0] = 0

            for v in children[u]:
                childDP = dfs(v, 0)  # child's parent is "not buying" in this branch
                newSkip = [NEG_INF] * (budget + 1)
                for c in range(budget + 1):
                    if dpSkip[c] == NEG_INF:
                        continue
                    for k in range(budget - c + 1):
                        if childDP[k] == NEG_INF:
                            continue
                        val = dpSkip[c] + childDP[k]
                        if val > newSkip[c + k]:
                            newSkip[c + k] = val
                dpSkip = newSkip

            # Case: u DOES buy
            # price depends on parentBuys
            if parentBuys == 0:
                buyCost = present[u]
            else:
                buyCost = present[u] // 2
            buyProfit = future[u] - buyCost

            # children of a buying u see parentBuys = True
            dpBuyChildren = [NEG_INF] * (budget + 1)
            dpBuyChildren[0] = 0
            for v in children[u]:
                childDP = dfs(v, 1)
                newBuy = [NEG_INF] * (budget + 1)
                for c in range(budget + 1):
                    if dpBuyChildren[c] == NEG_INF:
                        continue
                    for k in range(budget - c + 1):
                        if childDP[k] == NEG_INF:
                            continue
                        val = dpBuyChildren[c] + childDP[k]
                        if val > newBuy[c + k]:
                            newBuy[c + k] = val
                dpBuyChildren = newBuy

            dp = [NEG_INF] * (budget + 1)

            # Option 1: u skips
            for c in range(budget + 1):
                if dpSkip[c] > dp[c]:
                    dp[c] = dpSkip[c]

            # Option 2: u buys
            for c in range(budget + 1):
                if dpBuyChildren[c] == NEG_INF:
                    continue
                if c + buyCost <= budget:
                    val = dpBuyChildren[c] + buyProfit
                    if val > dp[c + buyCost]:
                        dp[c + buyCost] = val

            memo[key] = dp
            return dp

        dp_root = dfs(1, 0)  # CEO's parent doesn't buy
        return max(0, max(dp_root))