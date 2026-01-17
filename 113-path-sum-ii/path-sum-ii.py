# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(node: Optional[TreeNode], remaining: int):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            # if leaf and sum matches, save a copy of current path
            if not node.left and not node.right and remaining == 0:
                res.append(path[:])

            dfs(node.left, remaining)
            dfs(node.right, remaining)

            # backtrack
            path.pop()

        dfs(root, targetSum)
        return res