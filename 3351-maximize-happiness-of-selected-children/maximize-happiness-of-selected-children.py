class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        total = 0
        for i in range(k):
            gain = happiness[i] - i
            if gain <= 0:
                break
            total += gain
        return total