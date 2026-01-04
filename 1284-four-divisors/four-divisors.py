class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0

        for n in nums:
            cnt = 0
            s = 0
            d = 1
            limit = int(n ** 0.5)

            while d <= limit and cnt <= 4:
                if n % d == 0:
                    e = n // d
                    cnt += 1
                    s += d
                    if e != d:
                        cnt += 1
                        s += e
                d += 1

            if cnt == 4:
                total += s

        return total