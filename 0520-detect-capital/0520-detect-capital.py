class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return (
            word.isupper() or          # all capitals, e.g. "USA"
            word.islower() or          # all lowercase, e.g. "leetcode"
            (word[0].isupper() and word[1:].islower())  # title case, e.g. "Google"
        )