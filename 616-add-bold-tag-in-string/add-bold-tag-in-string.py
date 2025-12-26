class Solution(object):
    def addBoldTag(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        n = len(s)
        if not words:
            return s

        bold = [False] * n

        # Mark bold positions
        for i in range(n):
            for w in words:
                lw = len(w)
                if i + lw <= n and s[i:i + lw] == w:
                    for j in range(i, i + lw):
                        bold[j] = True

        # Build result with tags
        res = []
        i = 0
        while i < n:
            if not bold[i]:
                res.append(s[i])
                i += 1
            else:
                res.append("<b>")
                while i < n and bold[i]:
                    res.append(s[i])
                    i += 1
                res.append("</b>")

        return "".join(res)