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
    public TreeNode str2tree(String s) {
        if (s.isEmpty()) {
            return null;
        }

        int firstParen = s.indexOf('(');
        int value = (firstParen == -1) ? Integer.parseInt(s) : Integer.parseInt(s.substring(0, firstParen));
        TreeNode root = new TreeNode(value);

        if (firstParen == -1) {
            return root;
        }

        int start = firstParen;
        int leftParenCount = 0;

        for (int i = start; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                leftParenCount++;
            } else if (s.charAt(i) == ')') {
                leftParenCount--;
            }

            if (leftParenCount == 0 && start == firstParen) {
                root.left = str2tree(s.substring(start + 1, i));
                start = i + 1;
            } else if (leftParenCount == 0) {
                root.right = str2tree(s.substring(start + 1, i));
            }
        }

        return root;
    }
}