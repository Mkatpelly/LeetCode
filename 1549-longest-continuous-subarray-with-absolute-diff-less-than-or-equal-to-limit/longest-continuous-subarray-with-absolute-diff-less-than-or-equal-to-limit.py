class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_d = deque()  # indices, values non-increasing
        min_d = deque()  # indices, values non-decreasing
        left = 0
        ans = 0

        for right, x in enumerate(nums):
            # maintain max deque (decreasing)
            while max_d and nums[max_d[-1]] < x:
                max_d.pop()
            max_d.append(right)

            # maintain min deque (increasing)
            while min_d and nums[min_d[-1]] > x:
                min_d.pop()
            min_d.append(right)

            # shrink window until it satisfies the limit
            while nums[max_d[0]] - nums[min_d[0]] > limit:
                if max_d[0] == left:
                    max_d.popleft()
                if min_d[0] == left:
                    min_d.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans