class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        logs.sort(key=lambda x: x[0])
        
        # Union-Find setup
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True
        
        # Initially, n separate components
        components = n
        
        for timestamp, x, y in logs:
            if union(x, y):
                components -= 1
                if components == 1:
                    return timestamp
        
        return -1