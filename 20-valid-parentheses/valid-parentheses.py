class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        st = []

        for c in s:

            if c not in brackets:
                st.append(c)
            else:
                if not st or st.pop() != brackets[c]:
                    return False

        return len(st) == 0