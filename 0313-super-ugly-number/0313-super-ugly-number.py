class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        ugly = [0] * n
        ugly[0] = 1  # 1st super ugly number

        idx = [0] * k                 # indices into ugly[]
        vals = list(primes)           # current candidates = primes[j] * ugly[idx[j]]

        for i in range(1, n):
            # choose next super ugly number
            next_ugly = min(vals)
            ugly[i] = next_ugly

            # advance all primes that produced this min (avoid duplicates)
            for j in range(k):
                if vals[j] == next_ugly:
                    idx[j] += 1
                    vals[j] = ugly[idx[j]] * primes[j]

        return ugly[-1]