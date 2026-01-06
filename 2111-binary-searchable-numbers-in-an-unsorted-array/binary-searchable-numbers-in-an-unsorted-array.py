class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        prefix_max = [0] * n
        suffix_min = [0] * n

        # prefix_max[i] = max(nums[0..i])
        cur_max = float("-inf")
        for i in range(n):
            cur_max = max(cur_max, nums[i])
            prefix_max[i] = cur_max

        # suffix_min[i] = min(nums[i..n-1])
        cur_min = float("inf")
        for i in range(n - 1, -1, -1):
            cur_min = min(cur_min, nums[i])
            suffix_min[i] = cur_min

        count = 0
        for i in range(n):
            left_ok = (i == 0) or (prefix_max[i - 1] < nums[i])
            right_ok = (i == n - 1) or (suffix_min[i + 1] > nums[i])
            if left_ok and right_ok:
                count += 1

        return count