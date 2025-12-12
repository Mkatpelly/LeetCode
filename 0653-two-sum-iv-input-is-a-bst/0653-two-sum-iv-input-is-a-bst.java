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
    public boolean findTarget(TreeNode root, int k) {
        List<Integer> elements = new ArrayList<>();
        inOrderTraversal(root, elements);
        int left = 0, right = elements.size() - 1;
        
        while (left < right) {
            int sum = elements.get(left) + elements.get(right);
            if (sum == k) {
                return true;
            } else if (sum < k) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
    private void inOrderTraversal(TreeNode node, List<Integer> elements) {
        if (node == null) return;
        inOrderTraversal(node.left, elements);
        elements.add(node.val);
        inOrderTraversal(node.right, elements);
    }
}