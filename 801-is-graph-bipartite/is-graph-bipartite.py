class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n  # 0 = uncolored, 1 and -1 are the two colors

        for start in range(n):
            if color[start] != 0:
                continue

            # Start BFS from this component
            color[start] = 1
            queue = deque([start])

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == 0:
                        # Color neighbor with opposite color
                        color[v] = -color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        # Same color on both ends of an edge -> not bipartite
                        return False

        return True