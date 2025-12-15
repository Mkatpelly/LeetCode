# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        rows, cols = binaryMatrix.dimensions()
        r, c = 0, cols - 1
        ans = -1

        # Start at top-right and move only left or down
        while r < rows and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                ans = c        # found a 1, record column
                c -= 1         # try to find an even more left 1
            else:
                r += 1         # value is 0, go down to next row

        return ans