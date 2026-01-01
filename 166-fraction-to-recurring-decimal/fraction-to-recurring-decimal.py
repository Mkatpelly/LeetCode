class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        res = []

        # handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        # work with positive values as long
        num = abs(numerator)
        den = abs(denominator)

        # integer part
        integer_part = num // den
        res.append(str(integer_part))

        # remainder
        remainder = num % den
        if remainder == 0:
            return ''.join(res)

        res.append('.')

        # map remainder -> position in res where its digit starts
        pos = {}

        while remainder != 0:
            if remainder in pos:
                idx = pos[remainder]
                res.insert(idx, '(')
                res.append(')')
                break

            pos[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // den))
            remainder %= den

        return ''.join(res)