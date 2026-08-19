class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = []
        for i in s:
            if i.isalnum():
                new.append(i.lower())
        return new == new[::-1]