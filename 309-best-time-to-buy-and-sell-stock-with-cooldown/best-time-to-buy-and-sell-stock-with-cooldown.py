class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ht = {}

        def f(i, mode):
            nonlocal ht
            nonlocal n
            if i >= n:
                if mode == 1:
                    return 0
                else:
                    return -1e9
            
            if (i, mode) in ht:
                return ht[(i, mode)]
            
            if mode == 1:
                notbuy = f(i+1, mode)
                buy = -prices[i] + f(i+1, 2)
                ht[(i, mode)] = max(buy, notbuy)
                return ht[(i, mode)]
            
            else:
                notsell = f(i+1, mode)
                sell = prices[i] + f(i+2, 1)
                ht[(i, mode)] = max(sell, notsell)
                return ht[(i, mode)]
        
        return f(0, 1)