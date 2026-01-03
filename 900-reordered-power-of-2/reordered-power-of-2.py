class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        target = ''.join(sorted(str(n)))

        # 2^0 to 2^29 are <= 10^9
        for i in range(30):
            power_str = ''.join(sorted(str(1 << i)))
            if power_str == target:
                return True

        return False