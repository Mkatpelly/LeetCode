class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total = 0
        neg_count = 0
        min_abs = float('inf')

        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                abs_val = abs(val)
                total += abs_val
                if abs_val < min_abs:
                    min_abs = abs_val

        if neg_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs