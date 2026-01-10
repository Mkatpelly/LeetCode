class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def can_make(machine, x):
            total = 0
            for j in range(n):
                need = max(0, x * composition[machine][j] - stock[j])
                total += need * cost[j]
                if total > budget:
                    return False
            return True
        
        ans = 0
        
        for machine in range(k):
            lo, hi = 0, 10**9  # upper bound safe due to constraints
            
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if can_make(machine, mid):
                    lo = mid
                else:
                    hi = mid - 1
            
            ans = max(ans, lo)
        
        return ans
