class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # Each node is: {"children": {char: child_node}, "freq": int, "sent": str}
        self.root = {"children": {}, "freq": 0, "sent": ""}
        self.cur = []  # current input chars

        for s, t in zip(sentences, times):
            self._insert(s, t)

    def _insert(self, sentence: str, count: int) -> None:
        node = self.root
        for ch in sentence:
            if ch not in node["children"]:
                node["children"][ch] = {"children": {}, "freq": 0, "sent": ""}
            node = node["children"][ch]
        node["freq"] += count
        node["sent"] = sentence

    def input(self, c: str) -> List[str]:
        # End of sentence
        if c == '#':
            s = ''.join(self.cur)
            if s:
                self._insert(s, 1)
            self.cur = []
            return []

        # Add char to current prefix
        self.cur.append(c)
        prefix = ''.join(self.cur)

        # Walk the trie to the prefix node
        node = self.root
        for ch in prefix:
            if ch not in node["children"]:
                return []
            node = node["children"][ch]

        # DFS from this node to collect all sentences under this prefix
        res = []

        def dfs(n):
            if n["freq"] > 0:
                res.append((n["freq"], n["sent"]))
            for child in n["children"].values():
                dfs(child)

        dfs(node)

        # Sort: frequency desc, sentence asc
        res.sort(key=lambda x: (-x[0], x[1]))
        return [s for _, s in res[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)