class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = Counter(s)

        # Check if a palindromic permutation is possible
        odd_chars = [ch for ch, v in cnt.items() if v % 2 == 1]
        if len(odd_chars) > 1:
            return []

        # Middle character (for odd length), or empty for even length
        mid = odd_chars[0] if odd_chars else ""

        # Use up one occurrence of the middle character
        if mid:
            cnt[mid] -= 1

        res = []
        n = len(s)

        def dfs(cur):
            if len(cur) == n:
                res.append(cur)
                return

            for ch in list(cnt.keys()):
                if cnt[ch] >= 2:
                    cnt[ch] -= 2
                    dfs(ch + cur + ch)
                    cnt[ch] += 2

        dfs(mid)
        return res