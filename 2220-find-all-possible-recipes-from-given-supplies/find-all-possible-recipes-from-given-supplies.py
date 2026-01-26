class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)   # ingredient -> [recipes that need it]
        in_deg = defaultdict(int)   # recipe -> number of missing ingredients

        # Build graph and in-degree
        for rcp, ing_list in zip(recipes, ingredients):
            in_deg[rcp] = len(ing_list)
            for ing in ing_list:
                graph[ing].append(rcp)

        q = deque(supplies)
        ans = []

        # BFS (Kahn's algorithm style)
        while q:
            item = q.popleft()
            for rcp in graph[item]:
                in_deg[rcp] -= 1
                if in_deg[rcp] == 0:
                    ans.append(rcp)
                    q.append(rcp)

        return ans