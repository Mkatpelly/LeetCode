class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 1-indexed prefix sums for rows and columns
        row_ps = [[0] * (n + 1) for _ in range(m + 1)]
        col_ps = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_ps[i + 1][j + 1] = row_ps[i + 1][j] + grid[i][j]
                col_ps[i + 1][j + 1] = col_ps[i][j + 1] + grid[i][j]

        def is_magic(top: int, left: int, k: int) -> bool:
            bottom = top + k - 1
            right = left + k - 1

            # target sum = first row sum
            target = row_ps[top + 1][right + 1] - row_ps[top + 1][left]

            # check all rows
            for r in range(top + 1, bottom + 1):
                row_sum = row_ps[r + 1][right + 1] - row_ps[r + 1][left]
                if row_sum != target:
                    return False

            # check all columns
            for c in range(left, right + 1):
                col_sum = col_ps[bottom + 1][c + 1] - col_ps[top][c + 1]
                if col_sum != target:
                    return False

            # main diagonal
            diag1 = 0
            for d in range(k):
                diag1 += grid[top + d][left + d]
            if diag1 != target:
                return False

            # anti-diagonal
            diag2 = 0
            for d in range(k):
                diag2 += grid[top + d][right - d]
            if diag2 != target:
                return False

            return True

        # try from largest k down to 2
        max_k = min(m, n)
        for k in range(max_k, 1, -1):
            for i in range(0, m - k + 1):
                for j in range(0, n - k + 1):
                    if is_magic(i, j, k):
                        return k

        return 1