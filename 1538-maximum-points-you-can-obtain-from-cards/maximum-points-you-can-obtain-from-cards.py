class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k
        
        # If we take all cards
        if window_size == 0:
            return sum(cardPoints)
        
        total = sum(cardPoints)
        
        # Initial window
        curr = sum(cardPoints[:window_size])
        min_window = curr
        
        # Slide the window across the array
        for i in range(window_size, n):
            curr += cardPoints[i] - cardPoints[i - window_size]
            min_window = min(min_window, curr)
        
        return total - min_window
