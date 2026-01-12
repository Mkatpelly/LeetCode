class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            g[a].append(b)

        # base_valid: number of valid subarrays with all conflicts active
        # gain[x]: potential extra subarrays if we "ignore" conflicts that end at x
        gain = [0] * (n + 2)
        base_valid = 0
        best_gain = 0

        # r1: smallest right endpoint currently blocking
        # r2: second smallest right endpoint currently blocking
        r1 = n + 1
        r2 = n + 1

        # Sweep from right to left
        for i in range(n, 0, -1):
            # update r1, r2 with all conflicts (i, b)
            for b in g[i]:
                if b < r1:
                    r2 = r1
                    r1 = b
                elif b < r2:
                    r2 = b

            # all subarrays starting at i can extend up to r1 - 1
            base_valid += r1 - i

            # if we ignore the pair that first blocks at r1,
            # we can extend those subarrays further up to r2 - 1
            gain[r1] += r2 - r1
            if gain[r1] > best_gain:
                best_gain = gain[r1]

        return base_valid + best_gain