class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)

        dp[0] = 1
        pref[0] = 1

        max_dq = deque()  # indices, nums decreasing
        min_dq = deque()  # indices, nums increasing

        l = 0
        for r in range(n):
            # extend window with nums[r]
            while max_dq and nums[max_dq[-1]] <= nums[r]:
                max_dq.pop()
            max_dq.append(r)

            while min_dq and nums[min_dq[-1]] >= nums[r]:
                min_dq.pop()
            min_dq.append(r)

            # shrink from left while invalid
            while max_dq and min_dq and nums[max_dq[0]] - nums[min_dq[0]] > k:
                if max_dq[0] == l:
                    max_dq.popleft()
                if min_dq[0] == l:
                    min_dq.popleft()
                l += 1

            # all valid segments ending at r start from i in [l, r]
            # so dp[r+1] = sum_{i=l..r} dp[i] = pref[r] - pref[l-1]
            if l == 0:
                dp[r+1] = pref[r] % MOD
            else:
                dp[r+1] = (pref[r] - pref[l-1]) % MOD

            pref[r+1] = (pref[r] + dp[r+1]) % MOD

        return dp[n] % MOD