class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # prev2 = dp[i-2], prev1 = dp[i-1]
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, n):
            curr = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, curr

        return prev1