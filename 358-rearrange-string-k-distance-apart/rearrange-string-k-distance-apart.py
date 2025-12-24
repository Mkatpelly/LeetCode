class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k <= 1:
            return s

        # Count character frequencies
        freq = Counter(s)

        # Max-heap of (-count, char); sort items so ties are broken deterministically
        max_heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(max_heap)

        wait_q = deque()   # (cnt, ch) currently cooling down
        res = []

        while max_heap:
            cnt, ch = heapq.heappop(max_heap)  # cnt is negative
            res.append(ch)
            cnt += 1  # use one occurrence

            # Put this char into cooldown queue
            wait_q.append((cnt, ch))

            # When we have placed k chars since a char was used, it can re-enter the heap
            if len(wait_q) >= k:
                old_cnt, old_ch = wait_q.popleft()
                if old_cnt < 0:  # still remaining
                    heapq.heappush(max_heap, (old_cnt, old_ch))

        result = "".join(res)
        return result if len(result) == len(s) else ""