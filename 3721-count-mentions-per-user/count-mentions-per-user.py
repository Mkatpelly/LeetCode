class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        events.sort(key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))

        mentions = [0] * numberOfUsers
        # onlineUntil[i] = time when user i becomes online again;
        # user i is online at time t iff t >= onlineUntil[i]
        onlineUntil = [0] * numberOfUsers  # all online from time 0

        for etype, ts, data in events:
            t = int(ts)

            if etype == "OFFLINE":
                uid = int(data)
                # user goes offline for 60 time units
                onlineUntil[uid] = t + 60

            else:  # MESSAGE
                s = data
                if s == "ALL":
                    # mention all users, including offline
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif s == "HERE":
                    # mention all online users only
                    for i in range(numberOfUsers):
                        if onlineUntil[i] <= t:
                            mentions[i] += 1
                else:
                    # list of id<number> tokens, possibly duplicates
                    for token in s.split():
                        # token like "id7"
                        uid = int(token[2:])
                        mentions[uid] += 1

        return mentions