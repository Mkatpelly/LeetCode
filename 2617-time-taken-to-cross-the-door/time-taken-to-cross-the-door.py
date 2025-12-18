class Solution(object):
    def timeTaken(self, arrival, state):
        """
        :type arrival: List[int]
        :type state: List[int]
        :rtype: List[int]
        """
        n = len(arrival)
        ans = [-1] * n

        enter_q = deque()  # for state == 0
        exit_q = deque()   # for state == 1

        t = 0
        prev = -1  # -1: unused, 0: enter, 1: exit
        i = 0      # next person to enqueue

        while i < n or enter_q or exit_q:
            # If nobody is waiting, fast-forward time to next arrival
            if not enter_q and not exit_q and i < n and t < arrival[i]:
                t = arrival[i]
                prev = -1  # door unused before this second

            # Enqueue everyone who has arrived by current time t
            while i < n and arrival[i] <= t:
                if state[i] == 0:
                    enter_q.append(i)
                else:
                    exit_q.append(i)
                i += 1

            # If still no one is waiting (possible if arrival[i] > t)
            if not enter_q and not exit_q:
                # Next iteration will fast-forward time
                prev = -1
                continue

            # Decide direction based on prev
            if enter_q and exit_q:
                if prev == -1:
                    # unused last second -> exit first
                    use_exit = True
                elif prev == 0:
                    # entered last second -> enter first
                    use_exit = False
                else:  # prev == 1
                    # exited last second -> exit first
                    use_exit = True
            elif exit_q:
                use_exit = True
            else:
                use_exit = False

            if use_exit:
                idx = exit_q.popleft()
                prev = 1
            else:
                idx = enter_q.popleft()
                prev = 0

            ans[idx] = t
            t += 1

        return ans