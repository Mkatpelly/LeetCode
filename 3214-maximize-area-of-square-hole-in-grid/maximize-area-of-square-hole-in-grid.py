class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_consecutive(bars: List[int]) -> int:
            bars.sort()
            best = cur = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    cur += 1
                    if cur > best:
                        best = cur
                else:
                    cur = 1
            # number of unit gaps opened by a streak of length `best`
            return best + 1

        h_side = max_consecutive(hBars)
        v_side = max_consecutive(vBars)
        side = min(h_side, v_side)
        return side * side