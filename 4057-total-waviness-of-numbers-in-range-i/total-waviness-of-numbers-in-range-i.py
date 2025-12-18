class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def waviness(x):
            s = str(x)
            n = len(s)
            if n < 3:
                return 0
            w = 0
            for i in range(1, n - 1):
                if s[i] > s[i - 1] and s[i] > s[i + 1]:
                    w += 1  # peak
                elif s[i] < s[i - 1] and s[i] < s[i + 1]:
                    w += 1  # valley
            return w

        ans = 0
        for x in range(num1, num2 + 1):
            ans += waviness(x)
        return ans
