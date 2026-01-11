class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            # Update histogram heights for this row
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Largest rectangle in histogram for current heights
            stack = []  # will store indices
            for k in range(cols + 1):
                # Sentinel height 0 at the end to flush the stack
                curr_height = heights[k] if k < cols else 0
                while stack and curr_height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    # If stack is empty, width is k; else width is between stack[-1]+1 and k-1
                    w = k if not stack else k - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(k)

        return max_area