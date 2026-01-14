class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        res = list(s)
        total = 0  # suffix sum of shifts

        for i in range(n - 1, -1, -1):
            total = (total + shifts[i]) % 26
            # shift s[i] by total positions
            orig = ord(s[i]) - ord('a')
            res[i] = chr(ord('a') + (orig + total) % 26)

        return "".join(res)