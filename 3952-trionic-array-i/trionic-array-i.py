class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False  # need at least 3 non-empty segments

        # Phase 1: strictly increasing from index 0
        p = 0
        # stop at n-2 so that there is room for at least 2 more elements (for dec and final inc)
        while p < n - 2 and nums[p] < nums[p + 1]:
            p += 1

        # must have at least one increasing step, and not stop at 0
        if p == 0:
            return False

        # Phase 2: strictly decreasing starting from p
        q = p
        while q < n - 1 and nums[q] > nums[q + 1]:
            q += 1

        # need at least one decreasing step, and cannot reach the end here
        if q == p or q == n - 1:
            return False

        # Phase 3: strictly increasing from q to the end
        while q < n - 1 and nums[q] < nums[q + 1]:
            q += 1

        # valid trionic if we end exactly at the last index
        return q == n - 1