class NumArray(object):

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]  # keep original values
        self.bit = [0] * (self.n + 1)  # Fenwick tree
        
        # Build Fenwick tree
        for i, val in enumerate(nums):
            self._add(i + 1, val)
    
    def _add(self, i, delta):
        """Helper to add delta at position i in Fenwick tree"""
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    
    def _prefix_sum(self, i):
        """Helper to compute prefix sum up to index i"""
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    
    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)
    
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self._prefix_sum(right + 1) - self._prefix_sum(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)