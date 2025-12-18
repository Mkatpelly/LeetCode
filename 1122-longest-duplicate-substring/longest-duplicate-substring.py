class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return ""

        nums = [ord(c) - ord('a') for c in s]
        base = 26
        mod1 = 10**9 + 7
        mod2 = 10**9 + 9

        # precompute powers
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * base) % mod1
            pow2[i] = (pow2[i - 1] * base) % mod2

        def check(L):
            """Return start index of some duplicate substring of length L, else -1."""
            if L == 0:
                return -1
            h1 = h2 = 0
            for i in range(L):
                h1 = (h1 * base + nums[i]) % mod1
                h2 = (h2 * base + nums[i]) % mod2
            seen = {(h1, h2): [0]}
            for i in range(L, n):
                # remove leftmost char, add new char
                left = nums[i - L]
                h1 = (h1 * base - left * pow1[L] + nums[i]) % mod1
                h2 = (h2 * base - left * pow2[L] + nums[i]) % mod2
                key = (h1, h2)
                if key in seen:
                    for start in seen[key]:
                        if s[start:start + L] == s[i - L + 1:i + 1]:
                            return start
                    seen[key].append(i - L + 1)
                else:
                    seen[key] = [i - L + 1]
            return -1

        res_start = -1
        res_len = 0
        lo, hi = 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            idx = check(mid)
            if idx != -1:
                res_start, res_len = idx, mid
                lo = mid + 1
            else:
                hi = mid - 1

        return "" if res_start == -1 else s[res_start:res_start + res_len]