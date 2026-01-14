class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        mx = arr[0]
        cnt = 0

        for x in arr[1:]:
            if mx > x:
                cnt += 1
            else:
                mx = x
                cnt = 1
            if cnt == k:
                return mx

        # If no one reaches k before the end, mx is the global max and thus the winner
        return mx