class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # empty prefix
        s = 0
        ans = 0

        for x in nums:
            s += x
            ans += prefix_count.get(s - goal, 0)
            prefix_count[s] += 1

        return ans