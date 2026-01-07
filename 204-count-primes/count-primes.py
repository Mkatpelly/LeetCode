class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        # Only need to mark multiples for i up to sqrt(n)
        limit = int(n ** 0.5) + 1
        for i in range(2, limit):
            if is_prime[i]:
                # start from i*i, since smaller multiples already handled
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)