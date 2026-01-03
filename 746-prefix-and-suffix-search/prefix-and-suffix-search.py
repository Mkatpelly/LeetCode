class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.lookup = {}
        for idx, word in enumerate(words):
            L = len(word)
            # all non-empty prefixes and suffixes
            for p in range(1, L + 1):
                pref = word[:p]
                for s in range(1, L + 1):
                    suff = word[L - s:]
                    self.lookup[(pref, suff)] = idx

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        return self.lookup.get((pref, suff), -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)