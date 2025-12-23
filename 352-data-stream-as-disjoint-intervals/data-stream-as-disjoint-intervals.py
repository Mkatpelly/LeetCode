class SummaryRanges(object):

    def __init__(self):
        # list of [start, end], sorted by start
        self.intervals = []

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        intervals = self.intervals
        # Find insertion position by start
        i = bisect.bisect_left(intervals, [value, value])

        # Check if value is already within the previous interval
        if i > 0 and intervals[i - 1][0] <= value <= intervals[i - 1][1]:
            return

        # Check if value is already within the next interval
        if i < len(intervals) and intervals[i][0] <= value <= intervals[i][1]:
            return

        left_merge = (i > 0 and intervals[i - 1][1] + 1 == value)
        right_merge = (i < len(intervals) and intervals[i][0] - 1 == value)

        if left_merge and right_merge:
            # Merge three: previous, value, and next into one
            intervals[i - 1][1] = intervals[i][1]
            intervals.pop(i)
        elif left_merge:
            # Extend previous interval to include value
            intervals[i - 1][1] += 1
        elif right_merge:
            # Extend next interval to include value
            intervals[i][0] -= 1
        else:
            # Isolated value: create new interval [value, value]
            intervals.insert(i, [value, value])

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()