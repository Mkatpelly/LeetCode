class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        # Frequency map of all numbers on the right (initially whole array)
        right_counts = {}
        for v in nums:
            right_counts[v] = right_counts.get(v, 0) + 1

        left_counts = {}
        ans = 0

        for j, v in enumerate(nums):
            # Exclude the middle from the right side
            right_counts[v] -= 1
            if right_counts[v] == 0:
                # optional cleanup to keep dict smaller
                right_counts.pop(v)

            x = v * 2
            left = left_counts.get(x, 0)
            right = right_counts.get(x, 0)
            ans = (ans + left * right) % MOD

            # Include current value into the left side for future j
            left_counts[v] = left_counts.get(v, 0) + 1

        return ans % MOD
