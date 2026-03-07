class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n  = len(grid)   
        n2 = n//2

        y = ((grid[i][i], grid[n-i-1][n2],          #  <-- 1)
                grid[i][n-i-1]) for i in range(n2)) # 

        ctr1 = Counter(chain(*y))                   #  <-- 2)
        ctr1[grid[n2][n2]]+= 1                      #

        ctr2 = Counter(chain(*grid)) - ctr1         #  <-- 3)

        return n*n - max(                           #  <-- 4)
                ctr1[0]+ctr2[1], ctr1[1]+ctr2[0],
                ctr1[0]+ctr2[2], ctr1[2]+ctr2[0], 
                ctr1[1]+ctr2[2], ctr1[2]+ctr2[1])