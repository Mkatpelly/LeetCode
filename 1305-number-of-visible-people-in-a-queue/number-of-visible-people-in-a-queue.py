class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = [0] * n
        stack = []  # will store indices, heights strictly decreasing

        for i in range(n):
            # Current person i may be visible to some people on the stack
            while stack and heights[i] > heights[stack[-1]]:
                j = stack.pop()
                ans[j] += 1  # j can see i over all popped shorter people

            # If there is still someone on stack, they are taller than i
            # and can see i, but i blocks their view further.
            if stack:
                ans[stack[-1]] += 1

            stack.append(i)

        return ans
