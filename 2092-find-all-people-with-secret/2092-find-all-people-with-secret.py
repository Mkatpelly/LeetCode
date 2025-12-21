class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        know = [False] * n
        know[0] = True
        know[firstPerson] = True

        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        i = 0
        m = len(meetings)
        while i < m:
            t = meetings[i][2]

            # collect all meetings with the same time t
            j = i
            while j + 1 < m and meetings[j + 1][2] == t:
                j += 1

            # build temporary graph for this time block
            g = defaultdict(list)
            participants = set()
            for x, y, _ in meetings[i:j+1]:
                g[x].append(y)
                g[y].append(x)
                participants.add(x)
                participants.add(y)

            # BFS from participants who already know the secret
            q = deque()
            for p in participants:
                if know[p]:
                    q.append(p)

            visited = set(q)
            while q:
                u = q.popleft()
                for v in g[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)

            # everyone reached in this block now knows the secret
            for p in visited:
                know[p] = True

            i = j + 1

        return [i for i in range(n) if know[i]]
