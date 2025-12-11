class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s

        # Find longest palindromic prefix
        j = 0
        for i in range(n - 1, -1, -1):
            if s[i] == s[j]:
                j += 1

        if j == n:
            return s  # already a palindrome

        suffix = s[j:]           # non-palindromic tail
        rev_suffix = suffix[::-1]
        
        return rev_suffix + self.shortestPalindrome(s[:j]) + suffix