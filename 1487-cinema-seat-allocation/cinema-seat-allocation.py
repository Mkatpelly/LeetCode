class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        mp = {}

        for seat in reservedSeats:
            if seat[0] not in mp:
                mp[seat[0]] = []

            mp[seat[0]].append(seat[1])

        group = 0
        count = 0

        for row in mp:
            groupA = True
            groupB = True
            groupC = True

            count += 1

            for seat in mp[row]:
                if seat in [2, 3, 4, 5]:
                    groupA = False

                if seat in [4, 5, 6, 7]:
                    groupB = False

                if seat in [6, 7, 8, 9]:
                    groupC = False

            if groupA and groupC:
                group += 2
            elif groupA or groupB or groupC:
                group += 1

        group += (n - count) * 2

        return group