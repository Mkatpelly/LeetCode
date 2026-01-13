class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0.0
        maxY = 0.0
        for x, y, l in squares:
            total += float(l) * float(l)
            maxY = max(maxY, float(y + l))

        target = total / 2.0

        def area_below(h: float) -> float:
            area = 0.0
            for x, y, l in squares:
                y0 = float(y)
                ll = float(l)
                top = y0 + ll
                if h <= y0:
                    continue
                elif h >= top:
                    area += ll * ll
                else:
                    area += ll * (h - y0)
            return area

        lo, hi = 0.0, maxY
        # Binary search for sufficient precision
        for _ in range(60):
            mid = (lo + hi) / 2.0
            if area_below(mid) < target:
                lo = mid
            else:
                hi = mid

        return hi