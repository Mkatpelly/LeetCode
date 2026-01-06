class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # Connect stones that share a row or a column
        for i in range(n):
            x1, y1 = stones[i]
            for j in range(i + 1, n):
                x2, y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    union(i, j)

        # Count unique components
        roots = set(find(i) for i in range(n))
        components = len(roots)

        return n - components