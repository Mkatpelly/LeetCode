class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr: List[int]) -> bool:
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        ops = 0
        # Keep merging until the array is non-decreasing
        while not is_non_decreasing(nums):
            min_sum = float("inf")
            idx = 0  # leftmost index of the chosen pair

            # Find leftmost pair with minimum sum
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            # Merge that pair
            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            ops += 1

        return ops