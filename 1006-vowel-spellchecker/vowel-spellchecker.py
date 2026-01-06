class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def devowel(word: str) -> str:
            # Mask vowels in a lowercase word
            return "".join('*' if c in vowels else c for c in word)

        # 1. Exact words set
        exact = set(wordlist)

        # 2. Case-insensitive and 3. vowel-error maps
        case_map = {}
        vowel_map = {}

        for w in wordlist:
            lw = w.lower()

            # First occurrence for case-insensitive
            if lw not in case_map:
                case_map[lw] = w

            # First occurrence for vowel-error pattern
            pattern = devowel(lw)
            if pattern not in vowel_map:
                vowel_map[pattern] = w

        ans = []
        for q in queries:
            if q in exact:
                # Rule 1: exact match
                ans.append(q)
                continue

            lq = q.lower()
            if lq in case_map:
                # Rule 2: capitalization match
                ans.append(case_map[lq])
                continue

            pattern_q = devowel(lq)
            if pattern_q in vowel_map:
                # Rule 3: vowel error match
                ans.append(vowel_map[pattern_q])
                continue

            # No match
            ans.append("")

        return ans