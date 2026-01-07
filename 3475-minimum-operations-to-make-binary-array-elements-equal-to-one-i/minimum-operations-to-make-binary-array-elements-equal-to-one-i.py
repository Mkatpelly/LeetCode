class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 3)  # enough space for i+3 updates
        flip = 0
        ans = 0

        for i in range(n):
            flip += diff[i]
            cur = nums[i] ^ (flip & 1)  # effective bit after all flips so far

            if cur == 0:
                # need to flip window [i, i+2]
                if i + 2 >= n:
                    return -1
                ans += 1
                flip += 1
                diff[i + 3] -= 1  # effect ends after index i+2

        return ans