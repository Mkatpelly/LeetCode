# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        max_size = 0
    
        def dfs(node):
            nonlocal max_size
            if not node:
                return True, 0, float('inf'), float('-inf')  # is_bst, size, min_val, max_val
            left_is_bst, left_size, left_min, left_max = dfs(node.left)
            right_is_bst, right_size, right_min, right_max = dfs(node.right)
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                size = left_size + right_size + 1
                max_size = max(max_size, size)
                return True, size, min(left_min, node.val), max(right_max, node.val)
            else:
                return False, max(left_size, right_size), 0, 0
        
        dfs(root)
        return max_size