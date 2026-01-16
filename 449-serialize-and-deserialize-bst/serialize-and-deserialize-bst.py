# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""

        def inorder(node, elements):
            if not node:
                return None
            inorder(node.left, elements)
            elements.append(node.val)
            inorder(node.right, elements)

        def preorder(node, elements):
            if not node:
                return None
            elements.append(node.val)
            preorder(node.left, elements)
            preorder(node.right, elements)

        in_elements = []
        pre_elements = []
        inorder(root, in_elements)
        preorder(root, pre_elements)
        res = ",".join(str(i) for i in in_elements)
        res += "|"
        res += ",".join(str(i) for i in pre_elements)
        return res

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        split = data.split("|")
        inorder = [int(i) for i in split[0].split(",")]
        preorder = [int(i) for i in split[1].split(",")]

        def dfs(in_elements, pre_elements):
            if not in_elements or not pre_elements:
                return None
            val = pre_elements[0]
            root = TreeNode(val)

            for i in range(len(in_elements)):
                if in_elements[i] == val:
                    in_left = in_elements[:i]
                    in_right = in_elements[i+1:]
                    left_length = len(in_left)
                    pre_left = pre_elements[1: 1+left_length]
                    pre_right = pre_elements[1+left_length:]
                    root.left = dfs(in_left, pre_left)
                    root.right = dfs(in_right, pre_right)
                    break
            return root

        return dfs(inorder, preorder)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans