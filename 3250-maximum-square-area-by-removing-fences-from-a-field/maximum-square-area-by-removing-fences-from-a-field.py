MOD = 10**9 + 7

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def distances(fences: List[int], limit: int) -> set:
            # include boundary fences
            arr = fences + [1, limit]
            arr.sort()
            s = set()
            # all pairwise distances
            for i in range(len(arr)):
                for j in range(i):
                    s.add(arr[i] - arr[j])
            return s

        h_dist = distances(hFences, m)
        v_dist = distances(vFences, n)

        common = h_dist & v_dist
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD