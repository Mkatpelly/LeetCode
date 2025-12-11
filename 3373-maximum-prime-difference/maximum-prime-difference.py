class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_prime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        n = len(nums)

        # Find first prime index from the left
        left = 0
        while left < n and not is_prime(nums[left]):
            left += 1

        # Find first prime index from the right
        right = n - 1
        while right >= 0 and not is_prime(nums[right]):
            right -= 1

        return right - left