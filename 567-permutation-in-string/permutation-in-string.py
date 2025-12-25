class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n > m:
            return False

        # frequency arrays for 'a'..'z'
        cnt1 = [0] * 26
        cnt2 = [0] * 26

        for ch in s1:
            cnt1[ord(ch) - ord('a')] += 1

        # first window in s2
        for i in range(n):
            cnt2[ord(s2[i]) - ord('a')] += 1

        if cnt1 == cnt2:
            return True

        # slide window over s2
        for i in range(n, m):
            # add new char
            cnt2[ord(s2[i]) - ord('a')] += 1
            # remove char leaving window
            cnt2[ord(s2[i - n]) - ord('a')] -= 1

            if cnt1 == cnt2:
                return True

        return False