/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode recoverFromPreorder(String traversal) {
        Stack<TreeNode> stack = new Stack<>();
        int index = 0;
        while (index < traversal.length()) {
            int level = 0;
            while (index < traversal.length() && traversal.charAt(index) == '-') {
                level++;
                index++;
            }
            int valueStart = index;
            while (index < traversal.length() && Character.isDigit(traversal.charAt(index))) {
                index++;
            }
            int value = Integer.parseInt(traversal.substring(valueStart, index));
            TreeNode node = new TreeNode(value);
            while (stack.size() > level) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                TreeNode parent = stack.peek();
                if (parent.left == null) {
                    parent.left = node;
                } else {
                    parent.right = node;
                }
            }
            stack.push(node);
        }
        return stack.get(0);
    }
}