class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7

        # f[0] = 1 (no plots -> 1 way: empty)
        # f[1] = 2 (plot empty or filled)
        prev2 = 1  # f[0]
        prev1 = 2  # f[1]

        if n == 1:
            one_side = prev1
        else:
            for _ in range(2, n + 1):
                curr = (prev1 + prev2) % MOD  # f[i] = f[i-1] + f[i-2]
                prev2, prev1 = prev1, curr
            one_side = prev1

        # Both sides are independent
        return (one_side * one_side) % MOD