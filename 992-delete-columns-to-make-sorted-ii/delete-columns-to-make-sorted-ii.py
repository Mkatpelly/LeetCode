class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])
        
        # sorted[i] == True means strs[i] < strs[i+1] already fixed by previous columns
        sorted_pairs = [False] * (n - 1)
        deletions = 0
        
        for c in range(m):
            # Check if this column must be deleted
            bad = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][c] > strs[i + 1][c]:
                    bad = True
                    break
            
            if bad:
                # Delete this column
                deletions += 1
                continue
            
            # Column is safe; update permanently sorted pairs
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][c] < strs[i + 1][c]:
                    sorted_pairs[i] = True
        
        return deletions