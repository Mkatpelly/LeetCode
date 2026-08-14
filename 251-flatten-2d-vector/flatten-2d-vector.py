class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.r, self.c, self.v = 0, 0, v

    def next(self) -> int:
        while self.hasNext():
            ans = self.v[self.r][self.c]
            self.c += 1
            if len(self.v[self.r]) == self.c:
                self.r += 1
                self.c = 0
            return ans

    def hasNext(self) -> bool:
        while self.r < len(self.v) and len(self.v[self.r]) == 0:
            self.r += 1
            self.c = 0
            
        return self.r < len(self.v)
# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()