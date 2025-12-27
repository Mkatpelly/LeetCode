class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        current_max = float('-inf')

        # Initialize heap with the first element of each list
        for i, lst in enumerate(nums):
            val = lst[0]
            heapq.heappush(heap, (val, i, 0))
            current_max = max(current_max, val)

        best_range = [float('-inf'), float('inf')]

        while True:
            current_min, list_i, elem_i = heapq.heappop(heap)

            # Update best range if smaller
            if current_max - current_min < best_range[1] - best_range[0]:
                best_range = [current_min, current_max]

            # If this list is exhausted, we cannot continue
            if elem_i + 1 == len(nums[list_i]):
                break

            next_val = nums[list_i][elem_i + 1]
            heapq.heappush(heap, (next_val, list_i, elem_i + 1))

            # Update current max
            current_max = max(current_max, next_val)

        return best_range
