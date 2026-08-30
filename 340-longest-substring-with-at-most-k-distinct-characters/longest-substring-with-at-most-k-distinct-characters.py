class Solution:
    
    def lengthOfLongestSubstringKDistinct(self, string: str, numDistinctCharacters: int) -> int:
        
        freq = Counter()
        
        window_start = 0
        
        longest_valid_substring_seen = 0
        
        for window_end, char in enumerate(string):
            
            freq[char] += 1
            
            while len(freq) > numDistinctCharacters:
                
                left_char = string[window_start]
                
                freq[left_char] -= 1
                
                if freq[left_char] == 0:
                    del freq[left_char]
                
                window_start += 1
            
            window_size = window_end - window_start+1
            longest_valid_substring_seen = max(longest_valid_substring_seen, window_size)
        
        return longest_valid_substring_seen