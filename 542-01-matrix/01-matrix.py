class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()

        # Initialize distances: 0 stays 0, 1 becomes "unvisited" (inf)
        dist = [[float('inf')] * n for _ in range(m)]

        # Add all 0-cells to the queue
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))

        # BFS directions
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # Multi-source BFS
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # If we found a shorter path to this neighbor
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))

        return dist
