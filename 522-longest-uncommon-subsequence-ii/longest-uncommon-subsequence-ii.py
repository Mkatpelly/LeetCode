class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def is_subseq(a, b):
            """Return True if string a is a subsequence of string b."""
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
            return i == len(a)
        
        ans = -1
        n = len(strs)
        
        for i in range(n):
            unique = True
            for j in range(n):
                if i != j and is_subseq(strs[i], strs[j]):
                    unique = False
                    break
            if unique:
                ans = max(ans, len(strs[i]))
        
        return ans
