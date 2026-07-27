class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        r=len(grid)
        c=len(grid[0])
        max_area = 0
        moves = [(1,0),(0,1),(0,-1),(-1,0)]

        def run (sr,sc):

            queue = deque([(sr,sc)])
            area = 1
            grid[sr][sc]=0
            while queue:

                x,y = queue.popleft()
                
                for dx,dy in moves:

                    nr = x+dx
                    nc = y+dy

                    if 0<=nr<r and 0<=nc<c and grid[nr][nc]==1:
                        grid[nr][nc]=0
                        area+=1
                        queue.append((nr,nc))

            return area

        for row in range(r):
            for col in range(c):
                if grid[row][col]==1:
                    max_area = max(max_area,run(row,col))

        return max_area
        