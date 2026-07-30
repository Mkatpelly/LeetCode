class Solution(object):
    def countTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for x in nums:
            for y in nums:
                t = x & y
                freq[t] = freq.get(t, 0) + 1
        count = 0
        for z in nums:
            for key in freq:
                if key & z == 0:
                    count += freq[key]
        return count