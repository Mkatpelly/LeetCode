class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Min-heap of (time_so_far, node)
        heap = [(0, k)]
        # Shortest time to each node we have finalized
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue  # already found a better time
            dist[node] = time

            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + w, nei))

        if len(dist) != n:
            return -1
        return max(dist.values())