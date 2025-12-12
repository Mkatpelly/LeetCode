class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        MOUSE, CAT, DRAW = 1, 2, 0
        MOUSE_TURN, CAT_TURN = 0, 1

        # color[m][c][t]: 0 draw, 1 mouse win, 2 cat win
        color = [[[DRAW] * 2 for _ in range(n)] for __ in range(n)]
        # degree[m][c][t]: number of moves from this state
        degree = [[[0] * 2 for _ in range(n)] for __ in range(n)]

        # Initialize degrees
        for m in range(n):
            for c in range(n):
                degree[m][c][MOUSE_TURN] = len(graph[m])
                # cat cannot move to 0
                degree[m][c][CAT_TURN] = sum(1 for nb in graph[c] if nb != 0)

        q = deque()

        # Terminal states: mouse at hole -> mouse win
        for c in range(n):
            if c == 0:
                continue
            for t in (MOUSE_TURN, CAT_TURN):
                if color[0][c][t] == DRAW:
                    color[0][c][t] = MOUSE
                    q.append((0, c, t, MOUSE))

        # Terminal states: same position (not hole) -> cat win
        for i in range(1, n):
            for t in (MOUSE_TURN, CAT_TURN):
                if color[i][i][t] == DRAW:
                    color[i][i][t] = CAT
                    q.append((i, i, t, CAT))

        def prev_states(m, c, t):
            # current state (m, c, t); previous turn is 1 - t
            if t == MOUSE_TURN:
                # now mouse moves; previously cat moved to c
                pt = CAT_TURN
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    yield (m, pc, pt)
            else:
                # now cat moves; previously mouse moved to m
                pt = MOUSE_TURN
                for pm in graph[m]:
                    yield (pm, c, pt)

        while q:
            m, c, t, result = q.popleft()
            for pm, pc, pt in prev_states(m, c, t):
                if color[pm][pc][pt] != DRAW:
                    continue

                # If previous player can move to a state where they win, mark as win
                if (result == MOUSE and pt == MOUSE_TURN) or (result == CAT and pt == CAT_TURN):
                    color[pm][pc][pt] = result
                    q.append((pm, pc, pt, result))
                else:
                    # Otherwise, one losing move discovered; reduce degree
                    degree[pm][pc][pt] -= 1
                    # If all moves from (pm, pc, pt) lead to opponent wins,
                    # then (pm, pc, pt) is a loss for player to move.
                    if degree[pm][pc][pt] == 0:
                        lose = CAT if pt == MOUSE_TURN else MOUSE
                        color[pm][pc][pt] = lose
                        q.append((pm, pc, pt, lose))

        return color[1][2][MOUSE_TURN]