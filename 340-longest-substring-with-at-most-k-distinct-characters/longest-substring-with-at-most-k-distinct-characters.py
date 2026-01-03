class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0

        left = 0
        cnt = Counter()
        max_len = 0

        for right, ch in enumerate(s):
            cnt[ch] += 1

            # shrink window until at most k distinct characters remain
            while len(cnt) > k:
                left_ch = s[left]
                cnt[left_ch] -= 1
                if cnt[left_ch] == 0:
                    del cnt[left_ch]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len