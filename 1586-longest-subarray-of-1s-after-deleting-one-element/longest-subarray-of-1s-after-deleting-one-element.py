class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        best = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # Shrink window until it has at most 1 zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Window length minus 1 (because we must delete one element)
            best = max(best, right - left)
        
        return best
