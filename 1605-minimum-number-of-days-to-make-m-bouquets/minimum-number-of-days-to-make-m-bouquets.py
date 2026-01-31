class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        
        def isValid(mid):
            flowers = bouquets = 0
            for day in bloomDay:
                if day <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                        if bouquets >= m:
                            return True
                else:
                    flowers = 0
            return False
        
        l, r = min(bloomDay), max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            if isValid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l