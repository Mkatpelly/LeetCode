class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        # dp[i][j] = True if s[i..j] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # single chars
        for i in range(n):
            pal[i][i] = True

        # length >= 2
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        @lru_cache(None)
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            # option 1: skip position i
            best = dfs(i + 1)
            # option 2: take any palindrome starting at i with length >= k
            for j in range(i + k - 1, n):
                if pal[i][j]:
                    best = max(best, 1 + dfs(j + 1))
            return best
        return dfs(0)