class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Kadane for one array, also track prefix/suffix info
        total = 0
        max_sub = float('-inf')
        curr = 0

        # for prefix
        prefix_sum = 0
        best_prefix = float('-inf')

        # for suffix: we can compute later with total - min_prefix,
        # but easier here is to do a reverse pass or track directly.
        # Simpler: compute best_suffix via reverse Kadane.
        for x in arr:
            total += x
            curr = max(x, curr + x)
            max_sub = max(max_sub, curr)

            prefix_sum += x
            best_prefix = max(best_prefix, prefix_sum)
        suffix_sum = 0
        best_suffix = float('-inf')
        curr = 0
        for x in reversed(arr):
            suffix_sum += x
            best_suffix = max(best_suffix, suffix_sum)

        # Empty subarray allowed
        max_sub = max(max_sub, 0)

        if k == 1:
            return max_sub % MOD

        # For k >= 2
        ans = max_sub
        ans = max(ans, best_prefix + best_suffix)

        if total > 0:
            ans = max(ans, best_prefix + best_suffix + (k - 2) * total)

        return ans % MOD