class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        # window is over indices [1..n-1], inclusive, size at most dist+1
        L = 1
        R = 1

        # multiset `s` (smallest k-1 elements) and `t` (rest), both as sorted lists
        s = []   # holds values only
        t = []
        sum_s = 0

        def add(x):
            nonlocal sum_s
            # try to put x into s
            if len(s) < k - 1:
                insort(s, x)
                sum_s += x
            else:
                # s is full; compare with largest in s
                if s and x < s[-1]:
                    # move largest from s to t
                    v = s.pop()
                    sum_s -= v
                    insort(t, v)
                    # insert x into s
                    insort(s, x)
                    sum_s += x
                else:
                    insort(t, x)

        def remove(x):
            nonlocal sum_s
            # try to remove from s
            i = bisect_left(s, x)
            if i < len(s) and s[i] == x:
                sum_s -= x
                s.pop(i)
                # refill s from t if possible
                if t:
                    v = t.pop(0)
                    insort(s, v)
                    sum_s += v
            else:
                # must be in t
                j = bisect_left(t, x)
                if j < len(t) and t[j] == x:
                    t.pop(j)

        # initialize first window: indices [1 .. min(n-1, 1+dist)]
        R = 1
        while R < n and R <= 1 + dist:
            add(nums[R])
            R += 1

        ans = inf
        # slide window: L is left index of window in [1..n-1]
        while True:
            # current window is [L .. R-1]
            # we need at least k-1 elements to form k-1 additional starts
            if len(s) + len(t) >= k - 1:
                ans = min(ans, nums[0] + sum_s)

            # move window one step right
            if R >= n:    # R cannot go further; once L passes n-1, stop
                if L >= n - 1:
                    break
            if L + dist + 1 < n:
                # add new right element entering the window
                add(nums[L + dist + 1])
                R = L + dist + 2
            else:
                R = n  # no more additions

            # remove element leaving window
            remove(nums[L])
            L += 1
            if L >= n:
                break

        return ans