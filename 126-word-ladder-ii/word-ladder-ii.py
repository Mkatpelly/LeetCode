class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # parent relationships for shortest paths: child -> set of parents
        parents = defaultdict(set)

        # BFS frontier
        level = {beginWord}
        found = False
        L = len(beginWord)

        while level and not found:
            next_level = set()
            # remove all current level words from wordSet to avoid revisiting
            wordSet -= level

            for word in level:
                chars = list(word)
                for i in range(L):
                    orig = chars[i]
                    for c in range(ord('a'), ord('z') + 1):
                        ch = chr(c)
                        if ch == orig:
                            continue
                        chars[i] = ch
                        new_word = ''.join(chars)
                        if new_word in wordSet:
                            # record parent relation
                            parents[new_word].add(word)
                            next_level.add(new_word)
                            if new_word == endWord:
                                found = True
                    chars[i] = orig
            level = next_level

        if not found:
            return []

        # Backtrack all paths from endWord to beginWord using parents
        res = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                backtrack(p)
                path.pop()

        backtrack(endWord)
        return res