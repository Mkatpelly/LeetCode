class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                # Accumulate multi-digit numbers (e.g., '10')
                curr_num = curr_num * 10 + int(char)
                
            elif char == '[':
                # Save checkpoint (prefix string, multiplier) and reset
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
                
            elif char == ']':
                # Restore checkpoint and expand decoded inner string
                prev_str, num = stack.pop()
                curr_str = prev_str + (curr_str * num)
                
            else:
                # Append standard letters
                curr_str += char

        return curr_str