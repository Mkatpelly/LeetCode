class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        def can_cross(day):
            # 0 = land, 1 = water
            grid = [[0] * col for _ in range(row)]

            # Flood first `day` cells (1-based to 0-based)
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            q = deque()
            # Start BFS from all land cells in top row
            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    grid[0][j] = 1  # mark visited (treat as water to block revisits)

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while q:
                x, y = q.popleft()
                if x == row - 1:  # reached bottom
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append((nx, ny))
            return False

        left, right = 1, len(cells)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can_cross(mid):
                ans = mid        # can still cross; try later days
                left = mid + 1
            else:
                right = mid - 1  # cannot cross; try earlier days

        return ans