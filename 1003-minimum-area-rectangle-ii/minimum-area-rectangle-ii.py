class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        # Map: key = (mid_x, mid_y, dist2) -> list of point index pairs (i, j) forming diagonals
        diagonals = defaultdict(list)

        # Precompute all point pairs as potential diagonals
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                mid_x = x1 + x2      # store doubled midpoint to keep integers
                mid_y = y1 + y2
                dist2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
                diagonals[(mid_x, mid_y, dist2)].append((i, j))

        ans = inf

        # For each group of diagonals with same midpoint and length,
        # any two diagonals form a rectangle.
        for pairs in diagonals.values():
            m = len(pairs)
            if m < 2:
                continue
            # For each pair of diagonals, compute the rectangle area
            for a in range(m):
                i1, j1 = pairs[a]
                x1, y1 = points[i1]
                x2, y2 = points[j1]
                for b in range(a + 1, m):
                    i2, j2 = pairs[b]
                    x3, y3 = points[i2]
                    # Use x1,y1 and x3,y3 as adjacent vertices
                    # side1^2 = |P1 P3|^2
                    side1_sq = (x1 - x3) ** 2 + (y1 - y3) ** 2
                    # side2^2 = |P2 P3|^2  OR |P1 P4|^2; any adjacent side works
                    side2_sq = (x2 - x3) ** 2 + (y2 - y3) ** 2
                    area = sqrt(side1_sq * side2_sq)
                    if area < ans and area > 0:
                        ans = area

        return 0.0 if ans == inf else ans