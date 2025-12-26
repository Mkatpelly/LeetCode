class Excel(object):
    def __init__(self, height, width):
        self.h = height
        self.w = ord(width) - ord('A') + 1

        self.val = [[0] * self.w for _ in range(self.h)]
        self.formula = [[None] * self.w for _ in range(self.h)]
        self.dependents = defaultdict(set)  # (r,c) -> set of (r,c)

    def _col_to_idx(self, column):
        return ord(column) - ord('A')

    def _parse_ref(self, s):
        col = s[0]
        row = int(s[1:])
        return row - 1, self._col_to_idx(col)

    def _build_formula_map(self, numbers):
        fmap = defaultdict(int)
        for token in numbers:
            if ':' in token:
                left, right = token.split(':')
                r1, c1 = self._parse_ref(left)
                r2, c2 = self._parse_ref(right)
                for rr in range(r1, r2 + 1):
                    for cc in range(c1, c2 + 1):
                        fmap[(rr, cc)] += 1
            else:
                rr, cc = self._parse_ref(token)
                fmap[(rr, cc)] += 1
        return fmap

    def _clear_formula(self, r, c):
        old = self.formula[r][c]
        if old is not None:
            for (rr, cc) in old.keys():
                self.dependents[(rr, cc)].discard((r, c))
        self.formula[r][c] = None

    def _recompute_from_formula(self, r, c):
        f = self.formula[r][c]
        if f is None:
            return
        total = 0
        for (rr, cc), cnt in f.items():
            total += cnt * self.val[rr][cc]
        self.val[r][c] = total

    def _propagate(self, start_r, start_c):
        q = deque()
        q.append((start_r, start_c))
        visited = set()
        visited.add((start_r, start_c))

        while q:
            r, c = q.popleft()
            for dr, dc in list(self.dependents[(r, c)]):
                # This dependent cell's inputs changed; recompute its value
                self._recompute_from_formula(dr, dc)
                if (dr, dc) not in visited:
                    visited.add((dr, dc))
                    q.append((dr, dc))

    def set(self, row, column, val):
        r = row - 1
        c = self._col_to_idx(column)

        # Overwrite formula and dependencies
        self._clear_formula(r, c)

        # Set base value
        self.val[r][c] = val

        # Propagate this change through dependency graph
        self._propagate(r, c)

    def get(self, row, column):
        r = row - 1
        c = self._col_to_idx(column)
        return self.val[r][c]

    def sum(self, row, column, numbers):
        r = row - 1
        c = self._col_to_idx(column)

        # Remove old formula and its dependency links
        self._clear_formula(r, c)

        # Build and store new formula
        fmap = self._build_formula_map(numbers)
        self.formula[r][c] = fmap

        # Register reverse dependencies
        for (rr, cc) in fmap.keys():
            self.dependents[(rr, cc)].add((r, c))

        # Compute this cell from current values
        self._recompute_from_formula(r, c)

        # Propagate its new value to its dependents
        self._propagate(r, c)

        return self.val[r][c]
# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)