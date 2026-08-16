class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        rem = [0, 0, 0]

        for stone in stones:
            rem[stone % 3] += 1

        if rem[0] % 2 == 0:
            return rem[1] > 0 and rem[2] > 0

        return abs(rem[1] - rem[2]) > 2