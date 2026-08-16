class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtracking(
            i: int,
            j: int,
            path: str,
            next_index: int,
        ) -> bool:
            if path == word:
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if board[i][j] != word[next_index]:
                return False

            character = board[i][j]
            path += character
            board[i][j] = None

            found = (
                backtracking(i + 1, j, path, next_index + 1)
                or backtracking(i, j + 1, path, next_index + 1)
                or backtracking(i - 1, j, path, next_index + 1)
                or backtracking(i, j - 1, path, next_index + 1)
            )

            board[i][j] = character
            return found

        for k in range(m * n):
            i, j = divmod(k, n)
            if board[i][j] == word[0]:
                if backtracking(i, j, "", 0):
                    return True

        return False