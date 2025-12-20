class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        if not strs:
            return 0

        rows = len(strs)
        cols = len(strs[0])
        deletions = 0

        for c in range(cols):          # for each column
            for r in range(1, rows):   # check from second row downward
                if strs[r][c] < strs[r-1][c]:
                    deletions += 1
                    break              # this column is bad; go to next column

        return deletions