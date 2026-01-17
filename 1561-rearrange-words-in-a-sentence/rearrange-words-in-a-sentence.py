class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        # normalize to lowercase so the initial capital doesn't affect sorting
        words[0] = words[0].lower()

        # stable sort by length; equal-length words keep original order
        words.sort(key=len)

        # capitalize the first word of the rearranged sentence
        words[0] = words[0].capitalize()

        return " ".join(words)