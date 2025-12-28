class Solution(object):

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}  # maps used indices to swapped ones
        self.remaining = self.total

    def flip(self):
        # Pick a random index among remaining zeros
        r = random.randint(0, self.remaining - 1)

        # If r was swapped before, use its mapped value
        x = self.map.get(r, r)

        # Move the last available index into r's position
        self.remaining -= 1
        self.map[r] = self.map.get(self.remaining, self.remaining)

        # Convert flattened index to (i, j)
        return [x // self.n, x % self.n]

    def reset(self):
        self.map.clear()
        self.remaining = self.total

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()