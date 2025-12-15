class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        n = m // 3

        # left[i] = minimal sum of n elements chosen from nums[0..i]
        left = [0] * m
        max_heap = []
        curr_sum = 0

        for i in range(0, 2 * n):
            x = nums[i]
            curr_sum += x
            heapq.heappush(max_heap, -x)      # max-heap via negatives
            if len(max_heap) > n:
                curr_sum += heapq.heappop(max_heap)  # remove largest (negative)
            if len(max_heap) == n:
                left[i] = curr_sum

        # right[i] = maximal sum of n elements chosen from nums[i..m-1]
        right = [0] * (m + 1)  # extra slot for i = 2n
        min_heap = []
        curr_sum = 0

        for i in range(m - 1, n - 1, -1):
            x = nums[i]
            curr_sum += x
            heapq.heappush(min_heap, x)       # min-heap
            if len(min_heap) > n:
                curr_sum -= heapq.heappop(min_heap)  # remove smallest
            if len(min_heap) == n:
                right[i] = curr_sum

        ans = float('inf')
        # split between i and i+1, with i from n-1 to 2n-1
        for i in range(n - 1, 2 * n):
            diff = left[i] - right[i + 1]
            ans = min(ans, diff)

        return ans