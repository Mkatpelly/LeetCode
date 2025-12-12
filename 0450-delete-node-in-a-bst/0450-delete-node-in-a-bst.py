# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to delete found
            # Case 1 & 2: node has at most one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Case 3: node has two children
            # Find inorder successor (smallest in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left

            # Copy successor's value to current node
            root.val = successor.val
            # Delete successor node from right subtree
            root.right = self.deleteNode(root.right, successor.val)

        return root