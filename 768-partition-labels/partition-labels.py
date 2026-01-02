class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(s)}

        res = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                # close current partition
                res.append(end - start + 1)
                start = i + 1

        return res