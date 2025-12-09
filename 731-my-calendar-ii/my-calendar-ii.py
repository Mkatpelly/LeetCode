class MyCalendarTwo(object):

    def __init__(self):
        self.booked = []
        # store intervals that are already double booked
        self.overlaps = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        # Step 1: check against double-booked intervals
        for s, e in self.overlaps:
            if startTime < e and endTime > s:  # overlap exists
                return False  # would cause triple booking

        # Step 2: check against single-booked intervals
        for s, e in self.booked:
            if startTime < e and endTime > s:  # overlap exists
                # record the overlap as double booking
                self.overlaps.append((max(startTime, s), min(endTime, e)))

        # Step 3: add new booking
        self.booked.append((startTime, endTime))
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)