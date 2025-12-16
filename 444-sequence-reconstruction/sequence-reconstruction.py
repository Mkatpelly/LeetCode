class Solution(object):
    def sequenceReconstruction(self, nums, sequences):
        """
        :type nums: List[int]
        :type sequences: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        
        # Build graph and in-degrees (0-indexed)
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        
        # Add edges from each consecutive pair in every sequence
        for seq in sequences:
            for i in range(len(seq) - 1):
                a = seq[i]
                b = seq[i + 1]
                u = a - 1  # convert 1-indexed to 0-indexed
                v = b - 1
                graph[u].append(v)
                in_degree[v] += 1
        
        # Initialize queue with all nodes that have in-degree 0
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
        
        # Kahn's algorithm: the reconstruction is unique only if at each step
        # there is exactly one node with in-degree 0 (queue size == 1)
        while q:
            if len(q) > 1:
                # More than one choice → multiple valid orderings
                return False
            u = q.popleft()
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        
        # If we processed all nodes with exactly one choice at each step,
        # then nums is the only shortest supersequence
        return True