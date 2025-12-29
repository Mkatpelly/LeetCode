class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = {}
        for num in nums:
            key = num // 10         # XY: depth and position
            val = num % 10          # Z: node value
            mp[key] = val

        self.ans = 0

        def dfs(key, path_sum):
            if key not in mp:
                return

            # Add current node's value
            path_sum += mp[key]

            depth = key // 10
            pos = key % 10

            # Compute children keys
            left_pos = 2 * pos - 1
            right_pos = 2 * pos
            left_key = (depth + 1) * 10 + left_pos
            right_key = (depth + 1) * 10 + right_pos

            # If leaf: add path_sum
            if left_key not in mp and right_key not in mp:
                self.ans += path_sum
                return

            # Recurse into existing children
            dfs(left_key, path_sum)
            dfs(right_key, path_sum)

        # Root key from first number (array is ascending)
        root_key = nums[0] // 10
        dfs(root_key, 0)
        return self.ans