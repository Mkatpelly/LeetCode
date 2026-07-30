class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        leftProducts = [1] * n
        rightProducts = [1] * n
        result = [0] * n
        
        for i in range(1, n):
            leftProducts[i] = leftProducts[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            rightProducts[i] = rightProducts[i + 1] * nums[i + 1]
        
        for i in range(n):
            result[i] = leftProducts[i] * rightProducts[i]
        
        return result