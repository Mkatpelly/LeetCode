class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.k = n - len(blacklist)          # size of allowed range [0, k-1]
        black = set(blacklist)
        self.mp = {}

        # Start of the upper range [k, n-1]
        w = self.k

        for b in blacklist:
            # Only need to remap blacklisted numbers in [0, k-1]
            if b < self.k:
                # Find next non-blacklisted candidate in [k, n-1]
                while w in black:
                    w += 1
                self.mp[b] = w
                w += 1

    def pick(self):
        """
        :rtype: int
        """
        x = random.randrange(self.k)  # uniform in [0, k-1]
        return self.mp.get(x, x)

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()