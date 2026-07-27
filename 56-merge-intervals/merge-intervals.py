class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # 1. Sort by start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        for start, end in intervals:
            # If merged is empty or current interval does not overlap, append it
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                # Overlap: merge by extending the end
                merged[-1][1] = max(merged[-1][1], end)

        return merged