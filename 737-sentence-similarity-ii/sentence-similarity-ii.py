class Solution(object):
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2):
            return False

        parent = {}

        def find(x):
            # initialize parent lazily
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb

        # build union-find from similar pairs
        for a, b in similarPairs:
            union(a, b)

        # check each pair of words
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            # if either word is unseen or in different components, not similar
            if find(w1) != find(w2):
                return False

        return True