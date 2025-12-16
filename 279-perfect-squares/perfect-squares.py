class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # For each number from 1 to n
        for i in range(1, n + 1):
            # Try every perfect square j*j <= i
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        
        return dp[n]