class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        base = nums[0]
        # get the two smallest elements from the rest
        rest = sorted(nums[1:])
        return base + rest[0] + rest[1]