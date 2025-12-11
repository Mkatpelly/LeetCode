class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            # iterative Euclidean algorithm
            while b:
                a, b = b, a % b
            return a

        mn = min(nums)
        mx = max(nums)
        return gcd(mn, mx)