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
    private int preorderIndex;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        inorderIndexMap = new HashMap<>();
        preorderIndex = 0;
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }
        return buildSubTree(preorder, 0, inorder.length - 1);
    }
    private TreeNode buildSubTree(int[] preorder, int left, int right){
        if (left > right) return null;
        int rootValue = preorder[preorderIndex++];
        TreeNode root = new TreeNode(rootValue);
        root.left = buildSubTree(preorder, left, inorderIndexMap.get(rootValue) - 1);
        root.right = buildSubTree(preorder, inorderIndexMap.get(rootValue) + 1, right);

        return root;
    }
}