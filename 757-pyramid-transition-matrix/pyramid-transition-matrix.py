class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        mp = defaultdict(list)
        for triple in allowed:
            a, b, c = triple[0], triple[1], triple[2]
            mp[a + b].append(c)

        memo = {}  # row -> bool

        def dfs(row):
            if row in memo:
                return memo[row]
            if len(row) == 1:
                memo[row] = True
                return True

            n = len(row)
            choices = []
            for i in range(n - 1):
                pair = row[i:i+2]
                if pair not in mp:
                    memo[row] = False
                    return False
                choices.append(mp[pair])

            for cols in product(*choices):
                next_row = ''.join(cols)
                if dfs(next_row):
                    memo[row] = True
                    return True

            memo[row] = False
            return False

        return dfs(bottom)