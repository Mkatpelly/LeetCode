class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        def backtrack(length, visited: list):
            if length == n:
                return 0

            count = 0
            for i in range(10):
                if i == 0 and len(visited) == 0:
                    continue
                if i not in visited:
                    visited.append(i)
                    count += 1
                    count += backtrack(length + 1, visited)
                    visited.pop()
            return count

        return 1 + backtrack(0, [])