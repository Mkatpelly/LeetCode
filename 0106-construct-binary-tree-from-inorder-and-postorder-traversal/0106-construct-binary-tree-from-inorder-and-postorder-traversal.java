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
    private Map<Integer, Integer> inorderIndexMap;
    private int postorderIndex;
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        inorderIndexMap = new HashMap<>();
        postorderIndex = postorder.length - 1;
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }

        return buildSubTree(postorder, 0, inorder.length - 1);

    }

    private TreeNode buildSubTree(int[] postorder, int left, int right){
        if (left > right) return null;
        int rootValue = postorder[postorderIndex--];
        TreeNode root = new TreeNode(rootValue);
        root.right = buildSubTree(postorder, inorderIndexMap.get(rootValue) + 1, right);
        root.left = buildSubTree(postorder, left, inorderIndexMap.get(rootValue) - 1);
        return root;
    }
}