class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(corridor)

        # Collect indices of all seats
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        total_seats = len(seats)

        # If no seats or odd number of seats, no valid division
        if total_seats == 0 or total_seats % 2 == 1:
            return 0

        # If exactly two seats, corridor itself is exactly one section
        # There is exactly 1 way (only the fixed outer dividers)
        if total_seats == 2:
            return 1

        ways = 1
        # For each "gap" between consecutive seat-pairs
        # seat pairs: (S0,S1), (S2,S3), (S4,S5), ...
        for i in range(1, total_seats // 2):
            # End index of previous pair
            right_prev = seats[2 * i - 1]
            # Start index of next pair
            left_next = seats[2 * i]
            # Number of choices for divider is the number of positions
            # between right_prev and left_next
            gap = left_next - right_prev
            ways = (ways * gap) % MOD

        return ways