class WaveletNode:
    __slots__ = ['total_covered', 'lazy', 'left', 'right']
    def __init__(self):
        # Count of active units in this specific resolution block
        self.total_covered = 0
        # True if the entire dyadic block is 100% continuous saturated signal
        self.lazy = False
        # Multi-resolution sub-bands
        self.left = None
        self.right = None

class SparseWaveletIntervalEngine:
    def __init__(self):
        self.root = WaveletNode()
        self.DOMAIN_MIN = 0
        # The constraints bound the timeline up to 10^4
        self.DOMAIN_MAX = 10**4

    def inject_pulse(self, node: WaveletNode, start: int, end: int, val: int):
        """
        Injects a single coordinate point (a point pulse) into the wavelet domain.
        Maintains 100% exact integer determinism.
        """
        if node.lazy:
            return

        if start == end:
            node.total_covered = 1
            node.lazy = True
            return

        mid = (start + end) // 2
        if node.left is None:
            node.left = WaveletNode()
        if node.right is None:
            node.right = WaveletNode()

        if val <= mid:
            self.inject_pulse(node.left, start, mid, val)
        else:
            self.inject_pulse(node.right, mid + 1, end, val)

        node.total_covered = node.left.total_covered + node.right.total_covered
        
        # Pull up the saturation approximation if the entire block gets filled
        if node.total_covered == (end - start + 1):
            node.lazy = True

    def reconstruct_intervals(self, node: WaveletNode, start: int, end: int, current_stream: list[list[int]]):
        """
        Performs an in-order multi-resolution sweep to reconstruct disjoint interval boundaries.
        """
        if node is None or node.total_covered == 0:
            return

        # Macro-level shortcut: If this whole dyadic window is saturated, process it as a unit
        if node.lazy:
            if current_stream and current_stream[-1][1] + 1 == start:
                # Merge: If this block is contiguous with the previous interval, extend the right boundary
                current_stream[-1][1] = end
            else:
                # New disconnected interval found
                current_stream.append([start, end])
            return

        mid = (start + end) // 2
        # Deterministic chronological traversal (Left band then Right band)
        self.reconstruct_intervals(node.left, start, mid, current_stream)
        self.reconstruct_intervals(node.right, mid + 1, end, current_stream)

class SummaryRanges:

    def __init__(self):
        self.wavelet_matrix = SparseWaveletIntervalEngine()        

    def addNum(self, value: int) -> None:
        self.wavelet_matrix.inject_pulse(
            self.wavelet_matrix.root,
            self.wavelet_matrix.DOMAIN_MIN,
            self.wavelet_matrix.DOMAIN_MAX,
            value
        )        

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        self.wavelet_matrix.reconstruct_intervals(
            self.wavelet_matrix.root,
            self.wavelet_matrix.DOMAIN_MIN,
            self.wavelet_matrix.DOMAIN_MAX,
            intervals
        )
        return intervals        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
# obj.addNum(value)
# param_2 = obj.getIntervals()