# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        def dfs(tr, bl):
            x1, y1 = bl.x, bl.y
            x2, y2 = tr.x, tr.y

            # invalid rectangle
            if x1 > x2 or y1 > y2:
                return 0

            # no ships in this region
            if not sea.hasShips(tr, bl):
                return 0

            # single point, and hasShips == True => exactly one ship
            if x1 == x2 and y1 == y2:
                return 1

            midx = (x1 + x2) // 2
            midy = (y1 + y2) // 2

            # 4 quadrants:
            # top-right: [midx+1..x2] × [midy+1..y2]
            top_right = dfs(Point(x2, y2), Point(midx + 1, midy + 1))

            # top-left:  [x1..midx]   × [midy+1..y2]
            top_left = dfs(Point(midx, y2), Point(x1, midy + 1))

            # bottom-left: [x1..midx] × [y1..midy]
            bottom_left = dfs(Point(midx, midy), Point(x1, y1))

            # bottom-right: [midx+1..x2] × [y1..midy]
            bottom_right = dfs(Point(x2, midy), Point(midx + 1, y1))

            return top_right + top_left + bottom_left + bottom_right

        return dfs(topRight, bottomLeft)