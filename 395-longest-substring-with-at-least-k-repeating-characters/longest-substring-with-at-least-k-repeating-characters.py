class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(sub: str) -> int:
            # Base case: too short to have any valid substring
            if len(sub) < k:
                return 0

            # Frequency of characters in this substring
            freq = Counter(sub)

            # Find any character that is invalid (freq < k)
            for ch in freq:
                if freq[ch] < k:
                    # Split around this character and recurse on pieces
                    return max(helper(part) for part in sub.split(ch))

            # All characters occur at least k times: whole substring is valid
            return len(sub)

        return helper(s)