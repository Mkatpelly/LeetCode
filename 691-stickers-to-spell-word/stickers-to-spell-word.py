class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        n = len(stickers)
        # Precompute frequency counters for stickers
        sticker_cnts = [collections.Counter(s) for s in stickers]

        memo = {}

        def dfs(rem):
            # rem: remaining target string
            if not rem:
                return 0
            if rem in memo:
                return memo[rem]

            # Frequency of remaining target
            rem_cnt = collections.Counter(rem)

            ans = float('inf')
            for cnt in sticker_cnts:
                # pruning: if this sticker doesn't contain the first char, skip
                if rem[0] not in cnt:
                    continue

                # Build next remaining string after using this sticker once
                new_rem_chars = []
                for c in rem_cnt:
                    # remaining count after using this sticker once
                    left = rem_cnt[c] - cnt.get(c, 0)
                    if left > 0:
                        new_rem_chars.extend([c] * left)

                # Sort to normalize representation for memoization
                new_rem = ''.join(sorted(new_rem_chars))

                sub = dfs(new_rem)
                if sub != -1:
                    ans = min(ans, 1 + sub)

            memo[rem] = -1 if ans == float('inf') else ans
            return memo[rem]

        # sort target to normalize key
        target_sorted = ''.join(sorted(target))
        return dfs(target_sorted)