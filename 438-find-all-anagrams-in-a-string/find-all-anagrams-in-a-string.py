class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, k = len(s), len(p)
        if n < k:
            return []

        # Frequency arrays for 'a'..'z'
        need = [0] * 26
        window = [0] * 26

        for ch in p:
            need[ord(ch) - ord('a')] += 1

        # Initialize first window
        for i in range(k):
            window[ord(s[i]) - ord('a')] += 1

        res = []
        if window == need:
            res.append(0)

        # Slide the window
        for i in range(k, n):
            # Add new right char
            window[ord(s[i]) - ord('a')] += 1
            # Remove old left char
            left_char_idx = ord(s[i - k]) - ord('a')
            window[left_char_idx] -= 1

            if window == need:
                res.append(i - k + 1)

        return res