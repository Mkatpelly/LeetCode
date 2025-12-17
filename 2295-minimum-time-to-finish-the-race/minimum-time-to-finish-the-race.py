class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        INF = 10**18

        # best[k] = minimum time to run exactly k consecutive laps on a single tire (no change)
        best = [INF] * (numLaps + 1)

        for f, r in tires:
            lap_time = f
            total = 0
            k = 1
            while k <= numLaps and lap_time <= changeTime + f:
                total += lap_time
                # if total itself is already worse than starting fresh with some tire,
                # later k will only be worse, so we can still break on lap_time condition.
                if total < best[k]:
                    best[k] = total
                lap_time *= r
                k += 1

        # find largest k we ever filled
        maxk = 0
        for k in range(1, numLaps + 1):
            if best[k] < INF:
                maxk = k

        dp = [INF] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            # last k laps as one stint
            for k in range(1, min(i, maxk) + 1):
                if best[k] == INF:
                    continue
                if i == k:
                    cand = best[k]
                else:
                    cand = dp[i - k] + changeTime + best[k]
                if cand < dp[i]:
                    dp[i] = cand

        return dp[numLaps]