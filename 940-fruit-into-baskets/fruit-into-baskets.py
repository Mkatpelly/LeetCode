class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        left = 0
        max_len = 0

        for right, f in enumerate(fruits):
            count[f] += 1

            # shrink window if we have more than 2 types
            while len(count) > 2:
                lf = fruits[left]
                count[lf] -= 1
                if count[lf] == 0:
                    del count[lf]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len