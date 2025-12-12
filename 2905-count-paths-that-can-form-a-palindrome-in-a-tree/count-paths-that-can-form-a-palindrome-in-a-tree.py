class Solution(object):
    def countPalindromePaths(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        n = len(parent)
        g = [[] for _ in range(n)]
        # Build children list with edge bit
        for i in range(1, n):
            p = parent[i]
            c = s[i]
            bit = 1 << (ord(c) - ord('a'))
            g[p].append((i, bit))

        cnt = defaultdict(int)
        cnt[0] = 1  # mask 0 for root path
        ans = [0]   # use list so dfs can modify it

        def dfs(u, mask):
            for v, bit in g[u]:
                m = mask ^ bit

                # same mask -> all even counts
                ans[0] += cnt[m]

                # differ by one bit -> exactly one odd count
                for b in range(26):
                    ans[0] += cnt[m ^ (1 << b)]

                cnt[m] += 1
                dfs(v, m)

        dfs(0, 0)
        return ans[0]