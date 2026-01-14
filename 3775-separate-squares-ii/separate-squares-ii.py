class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        # Build all rectangles: [x1, x2] × [y1, y2]
        rects = []
        xs = set()
        ys = set()
        for x, y, l in squares:
            x1 = float(x)
            x2 = float(x + l)
            y1 = float(y)
            y2 = float(y + l)
            rects.append((x1, x2, y1, y2))
            xs.add(x1); xs.add(x2)
            ys.add(y1); ys.add(y2)

        xs = sorted(xs)
        ys = sorted(ys)

        if len(xs) == 1:  # degenerate but safe
            return ys[0]

        # Segment tree arrays (over x-intervals)
        n = len(xs) - 1           # number of x-intervals
        count = [0] * (4 * n)     # cover count
        covered = [0.0] * (4 * n) # covered length in this node

        def seg_update(idx, l, r, ql, qr, val):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                count[idx] += val
            else:
                mid = (l + r) // 2
                seg_update(idx * 2 + 1, l, mid, ql, qr, val)
                seg_update(idx * 2 + 2, mid, r, ql, qr, val)

            if count[idx] > 0:
                covered[idx] = xs[r] - xs[l]
            else:
                if l + 1 == r:
                    covered[idx] = 0.0
                else:
                    covered[idx] = covered[idx * 2 + 1] + covered[idx * 2 + 2]

        def seg_add(x1, x2, val):
            i = bisect.bisect_left(xs, x1)
            j = bisect.bisect_left(xs, x2)
            if i < j:
                seg_update(0, 0, n, i, j, val)

        # Prepare vertical events grouped by y
        events_by_y = [[] for _ in range(len(ys))]
        y_index = {y: i for i, y in enumerate(ys)}
        for x1, x2, y1, y2 in rects:
            events_by_y[y_index[y1]].append((x1, x2, +1))
            events_by_y[y_index[y2]].append((x1, x2, -1))

        # 1) Compute total union area
        total_area = 0.0
        for i in range(len(ys) - 1):
            # apply events at this y
            for x1, x2, typ in events_by_y[i]:
                seg_add(x1, x2, typ)
            width = covered[0]
            dy = ys[i + 1] - ys[i]
            total_area += width * dy

        target = total_area / 2.0

        # 2) Find minimal y where area below >= target
        # reset segtree
        count = [0] * (4 * n)
        covered = [0.0] * (4 * n)

        area = 0.0
        for i in range(len(ys) - 1):
            y_curr = ys[i]
            for x1, x2, typ in events_by_y[i]:
                seg_add(x1, x2, typ)
            width = covered[0]
            if width == 0:
                continue
            dy = ys[i + 1] - ys[i]
            strip_area = width * dy
            if area + strip_area >= target:
                # answer lies inside this strip
                remain = target - area
                return y_curr + remain / width
            area += strip_area

        return ys[-1]