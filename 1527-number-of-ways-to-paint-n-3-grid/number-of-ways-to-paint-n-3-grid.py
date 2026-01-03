class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # For row 1: 6 ABA, 6 ABC
        same = 6  # ABA-type
        diff = 6  # ABC-type

        for _ in range(n - 1):
            new_same = (3 * same + 2 * diff) % MOD
            new_diff = (2 * same + 2 * diff) % MOD
            same, diff = new_same, new_diff

        return (same + diff) % MOD