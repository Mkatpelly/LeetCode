# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # If root is the only node (leaf), boundary is just [root.val]
        if not root.left and not root.right:
            return [root.val]

        res = [root.val]

        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        def add_left_boundary(node: Optional[TreeNode]) -> None:
            cur = node
            while cur:
                if not is_leaf(cur):
                    res.append(cur.val)
                if cur.left:
                    cur = cur.left
                else:
                    cur = cur.right

        def add_leaves(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if is_leaf(node):
                res.append(node.val)
            else:
                add_leaves(node.left)
                add_leaves(node.right)

        def add_right_boundary(node: Optional[TreeNode]) -> None:
            cur = node
            tmp = []
            while cur:
                if not is_leaf(cur):
                    tmp.append(cur.val)
                if cur.right:
                    cur = cur.right
                else:
                    cur = cur.left
            # add in reverse order
            res.extend(reversed(tmp))

        # 1. Left boundary (excluding leaves), starting from root.left
        add_left_boundary(root.left)
        # 2. All leaves (both subtrees)
        add_leaves(root)
        # 3. Right boundary (excluding leaves), starting from root.right
        add_right_boundary(root.right)

        return res