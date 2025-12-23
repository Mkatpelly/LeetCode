class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        n = len(words)
        # map word -> index
        word_to_idx = {w: i for i, w in enumerate(words)}
        res = []

        def is_pal(s):
            return s == s[::-1]

        for i, w in enumerate(words):
            m = len(w)
            # split at every position: prefix = w[:k], suffix = w[k:]
            for k in range(m + 1):
                prefix = w[:k]
                suffix = w[k:]

                # case 1: suffix palindrome, need reversed prefix AFTER w
                #   w + rev(prefix)
                if is_pal(suffix):
                    rev_prefix = prefix[::-1]
                    j = word_to_idx.get(rev_prefix, -1)
                    if j != -1 and j != i:
                        res.append([i, j])

                # case 2: prefix palindrome, need reversed suffix BEFORE w
                #   rev(suffix) + w
                # k > 0 avoids duplicates when prefix == "" (already counted in case 1)
                if k > 0 and is_pal(prefix):
                    rev_suffix = suffix[::-1]
                    j = word_to_idx.get(rev_suffix, -1)
                    if j != -1 and j != i:
                        res.append([j, i])

        return res
