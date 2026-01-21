class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
                continue

            # Find first 0-bit from position 1 upward
            j = 1
            while ((num >> j) & 1) == 1:
                j += 1

            # Flip bit at position (j - 1)
            x = num ^ (1 << (j - 1))
            ans.append(x)

        return ans