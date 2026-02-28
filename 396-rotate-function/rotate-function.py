class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)

        def dp(i, memo: dict):
            if i not in memo:
                if i == 0:
                    memo[i] = 0
                    memo[i] += sum(j * nums[j] for j in range(n))
                    return memo[i]

                memo[i] = dp(i-1, memo) + s - n * nums[n-i]
            return memo[i]

        res = float('-inf')
        memo_dict = {}
        for k in range(n):
            res = max(res, dp(k, memo_dict))
        return res