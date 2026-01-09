class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # Pop all prices <= current price and accumulate their spans
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        # Push current price with its computed span
        self.stack.append((price, span))
        
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)