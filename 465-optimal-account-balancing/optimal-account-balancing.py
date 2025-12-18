class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        # 1) Build net balance for each person
        balance = defaultdict(int)
        for frm, to, amt in transactions:
            balance[frm] -= amt
            balance[to] += amt

        # Only non-zero balances matter
        debt = [v for v in balance.values() if v != 0]
        n = len(debt)
        if n == 0:
            return 0

        def dfs(start):
            # Move start to first non-zero balance
            while start < n and debt[start] == 0:
                start += 1
            if start == n:
                return 0  # all settled

            res = float('inf')
            seen = set()

            # Try to settle debt[start] with each later opposite-signed debt
            for i in range(start + 1, n):
                if debt[i] * debt[start] < 0 and debt[i] not in seen:
                    seen.add(debt[i])

                    # Settle start with i (partially or fully)
                    debt[i] += debt[start]
                    res = min(res, 1 + dfs(start + 1))
                    debt[i] -= debt[start]  # backtrack

                    # If we reached exact zero at i in this attempt,
                    # further choices are symmetric; we can prune.
                    if debt[i] + debt[start] == 0:
                        break

            return 0 if res == float('inf') else res

        return dfs(0)