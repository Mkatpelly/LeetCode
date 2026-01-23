class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly-linked list via arrays
        val = nums[:]                     # current value for each node
        prev = [-1] * n
        nxt = [-1] * n
        alive = [True] * n                # node still exists?

        for i in range(n):
            if i > 0:
                prev[i] = i - 1
            if i < n - 1:
                nxt[i] = i + 1

        # Count initial "descending" pairs
        decreasing = 0
        for i in range(n - 1):
            if val[i] > val[i + 1]:
                decreasing += 1

        # Min-heap of (pair_sum, left_index, version)
        # version is implicit via val[] & nxt[] checks; we detect stale entries.
        heap = []

        def push_pair(i: int):
            """Push pair (i, nxt[i]) into heap if valid."""
            j = nxt[i]
            if j != -1 and alive[i] and alive[j]:
                s = val[i] + val[j]
                heapq.heappush(heap, (s, i))

        # Initialize heap with all adjacent pairs
        for i in range(n - 1):
            push_pair(i)

        ops = 0

        # Helper to check if current array is non-decreasing: use 'decreasing' == 0
        while decreasing > 0:
            # Get leftmost minimal-sum valid pair
            while True:
                if not heap:
                    # Should not happen in valid inputs
                    return ops
                pair_sum, i = heapq.heappop(heap)
                j = nxt[i]
                # Check if this pair is still valid (both alive and adjacent)
                if j != -1 and alive[i] and alive[j] and val[i] + val[j] == pair_sum:
                    break
                # otherwise it's stale, skip it

            j = nxt[i]  # right index

            # Before merging, update decreasing count around (i, j)

            # Pair (i, j) was contributing if val[i] > val[j]
            if val[i] > val[j]:
                decreasing -= 1

            # Pair (prev[i], i) may have been contributing, will be affected
            pi = prev[i]
            if pi != -1 and alive[pi]:
                if val[pi] > val[i]:
                    decreasing -= 1

            # Pair (j, nxt[j]) may have been contributing, will disappear
            nj = nxt[j]
            if nj != -1 and alive[nj]:
                if val[j] > val[nj]:
                    decreasing -= 1

            # Merge j into i
            val[i] += val[j]
            alive[j] = False

            # Remove j from the linked list
            nxt[i] = nj
            if nj != -1:
                prev[nj] = i

            # Now re-count possible new descending pairs around i

            # (prev[i], i)
            if pi != -1 and alive[pi]:
                if val[pi] > val[i]:
                    decreasing += 1

            # (i, nxt[i])
            if nj != -1 and alive[nj]:
                if val[i] > val[nj]:
                    decreasing += 1

            # Push updated adjacent pairs into heap
            if pi != -1 and alive[pi]:
                push_pair(pi)
            push_pair(i)

            ops += 1

        return ops