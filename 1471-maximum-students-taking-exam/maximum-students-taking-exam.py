class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        m, n = len(seats), len(seats[0])

        # Step 1: good seats bitmask per row
        good_mask = [0] * m
        for i in range(m):
            mask = 0
            for j in range(n):
                if seats[i][j] == '.':
                    mask |= (1 << j)
            good_mask[i] = mask

        # Step 2–3: precompute valid masks per row
        all_masks = range(1 << n)
        valid = [[] for _ in range(m)]

        def ok_row(mask, row):
            # only use good seats
            if (mask & ~good_mask[row]) != 0:
                return False
            # no adjacent students in same row
            if (mask & (mask << 1)) != 0:
                return False
            return True

        for r in range(m):
            for mask in all_masks:
                if ok_row(mask, r):
                    valid[r].append(mask)

        # Step 4–5: DP
        from collections import defaultdict
        dp_prev = defaultdict(lambda: -1)
        for mask in valid[0]:
            dp_prev[mask] = bin(mask).count("1")

        for r in range(1, m):
            dp_curr = defaultdict(lambda: -1)
            for curr in valid[r]:
                cnt = bin(curr).count("1")
                for prev in dp_prev:
                    if dp_prev[prev] < 0:
                        continue
                    # no diagonal cheating with row r-1
                    if (curr & (prev << 1)) != 0:
                        continue
                    if (curr & (prev >> 1)) != 0:
                        continue
                    dp_curr[curr] = max(dp_curr[curr], dp_prev[prev] + cnt)
            dp_prev = dp_curr

        return max(dp_prev.values() or [0])