class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbr_map = collections.defaultdict(set)
        for w in dictionary:
            a = self._abbr(w)
            self.abbr_map[a].add(w)

    def _abbr(self, word):
        if len(word) < 3:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        a = self._abbr(word)
        # No word in dictionary has this abbreviation.
        if a not in self.abbr_map:
            return True
        # Only the same word(s) have this abbreviation.
        s = self.abbr_map[a]
        return len(s) == 1 and word in s


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)