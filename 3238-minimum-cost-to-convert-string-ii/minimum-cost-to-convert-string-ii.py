class TrieNode:
    __slots__ = ("child", "id")
    def __init__(self):
        self.child = {}   # char -> TrieNode
        self.id = -1      # pattern id if this node is a pattern end


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        n = len(source)
        if n != len(target):
            return -1

        # 1) Build trie from ALL strings in original + changed, assign each a pattern id.
        root = TrieNode()
        patterns = []  # id -> string (optional, not strictly needed)

        def insert(s: str) -> int:
            node = root
            for ch in s:
                if ch not in node.child:
                    node.child[ch] = TrieNode()
                node = node.child[ch]
            if node.id == -1:
                node.id = len(patterns)
                patterns.append(s)
            return node.id

        for s in original:
            insert(s)
        for s in changed:
            insert(s)

        m = len(patterns)
        if m == 0:
            return 0 if source == target else -1

        # 2) Build all-pairs shortest path on pattern graph via Floyd–Warshall.
        g = [[inf] * m for _ in range(m)]
        for i in range(m):
            g[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u = insert(o)   # existing
            v = insert(c)   # existing
            if w < g[u][v]:
                g[u][v] = w

        for k in range(m):
            gk = g[k]
            for i in range(m):
                gi = g[i]
                if gi[k] == inf:
                    continue
                ik = gi[k]
                for j in range(m):
                    if gk[j] == inf:
                        continue
                    new_cost = ik + gk[j]
                    if new_cost < gi[j]:
                        gi[j] = new_cost

        # 3) Precompute, for every starting index i, all pattern endings in source and target.

        # source_match[i] = list of (end_index, pattern_id) for substrings source[i..end_index]
        source_match = [[] for _ in range(n)]
        target_match = [[] for _ in range(n)]

        # Walk source through trie
        for i in range(n):
            node = root
            j = i
            while j < n and source[j] in node.child:
                node = node.child[source[j]]
                if node.id != -1:
                    source_match[i].append((j, node.id))
                j += 1

        # Walk target through trie
        for i in range(n):
            node = root
            j = i
            while j < n and target[j] in node.child:
                node = node.child[target[j]]
                if node.id != -1:
                    target_match[i].append((j, node.id))
                j += 1

        # 4) DP: dp[i] = min cost to convert source[i:] to target[i:].
        dp = [inf] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            # Option 1: keep char if equal
            if source[i] == target[i]:
                if dp[i + 1] < dp[i]:
                    dp[i] = dp[i + 1]

            # Option 2: transform substring starting at i
            if dp[i] == 0 and source[i] == target[i]:
                # nothing to improve, but keep general handling; no early break
                pass

            # Try all pattern matches from source[i]
            if not source_match[i] or not target_match[i]:
                continue

            # For fast intersection by end index, build map for target endings at i
            # end -> list of (pattern_id_target)
            end_to_target_ids = {}
            for end_t, id_t in target_match[i]:
                end_to_target_ids.setdefault(end_t, []).append(id_t)

            for end_s, id_s in source_match[i]:
                if end_s not in end_to_target_ids:
                    continue
                # same end index -> same length substring [i..end_s]
                if dp[end_s + 1] == inf:
                    continue
                for id_t in end_to_target_ids[end_s]:
                    cst = g[id_s][id_t]
                    if cst == inf:
                        continue
                    total = cst + dp[end_s + 1]
                    if total < dp[i]:
                        dp[i] = total

        return -1 if dp[0] == inf else dp[0]