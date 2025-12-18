class DetectSquares(object):

    def __init__(self):
        # count of each point (x, y)
        self.cnt = defaultdict(int)
        # points grouped by y (row): y -> {x: count}
        self.rows = defaultdict(lambda: defaultdict(int))

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        x, y = point
        self.cnt[(x, y)] += 1
        self.rows[y][x] += 1

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        x, y = point
        if y not in self.rows:
            return 0

        res = 0
        # iterate over all points in the same row as query
        row = self.rows[y]
        for x2, c_row in row.items():
            if x2 == x:
                continue
            side = abs(x2 - x)
            # possible y-coordinates for the square (above and below)
            for y2 in (y + side, y - side):
                # corners: (x, y2) and (x2, y2), diagonal: (x2, y)
                c1 = self.cnt.get((x, y2), 0)
                c2 = self.cnt.get((x2, y2), 0)
                if c1 and c2:
                    res += c_row * c1 * c2
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)