class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left, right = max(weights), sum(weights)

        # Check if we can ship within 'days' using capacity 'cap'
        def can_ship(cap):
            needed_days = 1
            curr = 0
            for w in weights:
                if curr + w > cap:
                    needed_days += 1
                    curr = 0
                curr += w
                if needed_days > days:
                    return False
            return True

        # Binary search for minimal feasible capacity
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left