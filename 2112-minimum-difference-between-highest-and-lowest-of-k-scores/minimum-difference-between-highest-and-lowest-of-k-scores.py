class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        # If k == 1, the answer is always 0, but the loop also handles it.
        ans = float('inf')
        for i in range(n - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans