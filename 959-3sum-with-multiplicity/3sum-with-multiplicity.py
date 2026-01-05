class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Count frequencies of each value 0..100
        cnt = [0] * 101
        for v in arr:
            cnt[v] += 1

        ans = 0

        # Enumerate value triples x <= y <= z
        for x in range(101):
            if cnt[x] == 0:
                continue
            for y in range(x, 101):
                if cnt[y] == 0:
                    continue
                z = target - x - y
                if z < 0 or z > 100:
                    continue
                if z < y:  # enforce y <= z
                    continue
                if cnt[z] == 0:
                    continue

                if x == y == z:
                    c = cnt[x]
                    if c >= 3:
                        ans += c * (c - 1) * (c - 2) // 6
                elif x == y != z:
                    c1, c2 = cnt[x], cnt[z]
                    if c1 >= 2:
                        ans += c1 * (c1 - 1) // 2 * c2
                elif x != y == z:
                    c1, c2 = cnt[x], cnt[y]
                    if c2 >= 2:
                        ans += c1 * (c2 * (c2 - 1) // 2)
                else:  # x < y < z
                    ans += cnt[x] * cnt[y] * cnt[z]

                ans %= MOD

        return ans