class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 2:
            return n

        left = 0
        count = {}
        max_len = 0

        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1

            # shrink window until we have at most 2 distinct chars
            while len(count) > 2:
                left_ch = s[left]
                count[left_ch] -= 1
                if count[left_ch] == 0:
                    del count[left_ch]
                left += 1

            # window [left, right] has at most 2 distinct chars
            max_len = max(max_len, right - left + 1)

        return max_len