class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        # counts balance for digits 0-9
        cnt = [0] * 10

        for s_ch, g_ch in zip(secret, guess):
            if s_ch == g_ch:
                bulls += 1
            else:
                s = ord(s_ch) - ord('0')
                g = ord(g_ch) - ord('0')

                # if guess had extra 's' before, now we match one -> cow
                if cnt[s] < 0:
                    cows += 1
                # if secret had extra 'g' before, now we match one -> cow
                if cnt[g] > 0:
                    cows += 1

                cnt[s] += 1
                cnt[g] -= 1

        return str(bulls) + "A" + str(cows) + "B"