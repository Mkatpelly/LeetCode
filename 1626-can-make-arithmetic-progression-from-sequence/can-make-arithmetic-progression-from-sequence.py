class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        
        # If there are only 1 or 2 elements, they always form an AP
        if len(arr) <= 2:
            return True
        
        # The common difference should be the same between every consecutive pair
        d = arr[1] - arr[0]
        
        # Check that arr[i] - arr[i-1] == d for all i from 2 to len(arr)-1
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != d:
                return False
        
        return True