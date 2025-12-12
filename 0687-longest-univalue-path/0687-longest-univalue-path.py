# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0

        def dfs(node):
            if not node:
                return 0

            # longest downward paths from children
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            left_path = right_path = 0

            if node.left and node.left.val == node.val:
                left_path = left_len + 1
            if node.right and node.right.val == node.val:
                right_path = right_len + 1

            # update global best using both sides through this node
            self.ans = max(self.ans, left_path + right_path)

            # return longest single branch upward
            return max(left_path, right_path)

        dfs(root)
        return self.ans