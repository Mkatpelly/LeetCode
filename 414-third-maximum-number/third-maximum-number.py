class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        Max = max(nums)
        secondMax = min(nums)
        thirdMax = float("-inf")

        for i in range(n):
            if nums[i] < Max and nums[i]  > secondMax:
                thirdMax = secondMax
                secondMax = nums[i]
            elif nums[i] < secondMax and nums[i] > thirdMax:
                thirdMax = nums[i]
            else:
                pass

        if len(set(nums)) >= 3:
            result = thirdMax
        else:
            result = Max
        return result
