class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 7:
            return False

        # prefix sums: pre[i] = sum(nums[0..i])
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]

        total = pre[-1]

        # choose middle cut j
        for j in range(3, n - 3):
            seen = set()

            # find i on the left side
            for i in range(1, j - 1):
                if pre[i - 1] == pre[j - 1] - pre[i]:
                    seen.add(pre[i - 1])

            # find k on the right side
            for k in range(j + 2, n - 1):
                if pre[k - 1] - pre[j] == total - pre[k]:
                    if pre[k - 1] - pre[j] in seen:
                        return True

        return False