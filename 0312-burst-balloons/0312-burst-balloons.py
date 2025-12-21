class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        balloons = [1] + [x for x in nums if x > 0] + [1]
        n = len(balloons)

        # dp[i][j] = max coins from bursting balloons in (i, j), exclusive
        dp = [[0] * n for _ in range(n)]

        # length is the distance between i and j
        for length in range(2, n):           # at least one balloon in between
            for left in range(0, n - length):
                right = left + length
                # Try each balloon k as the last to burst in (left, right)
                best = 0
                for k in range(left + 1, right):
                    coins = (balloons[left] * balloons[k] * balloons[right] +
                             dp[left][k] + dp[k][right])
                    if coins > best:
                        best = coins
                dp[left][right] = best

        return dp[0][n - 1]