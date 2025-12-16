class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # Use a list to hold the component count so we can modify it in dfs
        components = [0]
        
        def dfs(node, parent):
            # Start with the current node's value
            total = values[node]
            
            # Visit all children (neighbors except parent)
            for neighbor in adj[node]:
                if neighbor != parent:
                    total += dfs(neighbor, node)
            
            # If the subtree sum is divisible by k, we can cut it off as a component
            if total % k == 0:
                components[0] += 1
            
            return total
        dfs(0, -1)
        return components[0]
