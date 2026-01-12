class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1  # empty prefix has remainder 0

        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            # normalize remainder into [0, k-1]
            r = ((prefix % k) + k) % k
            ans += freq[r]
            freq[r] += 1

        return ans