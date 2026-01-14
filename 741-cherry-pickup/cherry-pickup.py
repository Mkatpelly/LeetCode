class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def dp(r1: int, c1: int, c2: int) -> int:
            # r2 is implied by steps equality: r1 + c1 == r2 + c2
            r2 = r1 + c1 - c2

            # bounds and thorn checks
            if not (0 <= r1 < n and 0 <= c1 < n and
                    0 <= r2 < n and 0 <= c2 < n):
                return float("-inf")
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")

            # base: both at bottom-right
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            # cherries at current cells
            cherries = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]

            # move both walkers (down or right)
            best_next = max(
                dp(r1 + 1, c1,     c2    ),  # down, down
                dp(r1 + 1, c1,     c2 + 1),  # down, right
                dp(r1,     c1 + 1, c2    ),  # right, down
                dp(r1,     c1 + 1, c2 + 1)   # right, right
            )

            if best_next == float("-inf"):
                return float("-inf")

            return cherries + best_next

        ans = dp(0, 0, 0)
        return max(ans, 0)