class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        if n % groupSize != 0:
            return False

        cnt = Counter(hand)
        keys = sorted(cnt.keys())

        for x in keys:
            c = cnt[x]
            if c == 0:
                continue
            # we need c sequences starting from x
            for v in range(x, x + groupSize):
                if cnt[v] < c:
                    return False
                cnt[v] -= c

        return True