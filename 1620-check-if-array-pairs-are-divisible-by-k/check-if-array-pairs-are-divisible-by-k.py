class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0] * k

        # Count normalized remainders
        for x in arr:
            r = ((x % k) + k) % k  # handle negatives
            cnt[r] += 1

        # Remainder 0 must pair with itself
        if cnt[0] % 2 != 0:
            return False

        # Check complementary remainders
        for r in range(1, k):
            if cnt[r] != cnt[k - r]:
                return False

        return True