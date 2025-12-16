class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, 0, 0]  
        for x in nums:
            old_dp = dp[:]
            for r in range(3):
                if old_dp[r] != -1 or r == 0:  
                    new_sum = old_dp[r] + x
                    new_r = new_sum % 3
                    dp[new_r] = max(dp[new_r], new_sum)
        
        return dp[0]