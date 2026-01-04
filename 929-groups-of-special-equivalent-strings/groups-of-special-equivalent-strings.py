class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        signatures = set()

        for w in words:
            even = sorted(w[0::2])
            odd = sorted(w[1::2])
            signatures.add((''.join(even), ''.join(odd)))

        return len(signatures)