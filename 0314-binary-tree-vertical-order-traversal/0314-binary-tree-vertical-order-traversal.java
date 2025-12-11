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
    public List<List<Integer>> verticalOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }

        TreeMap<Integer, List<int[]>> map = new TreeMap<>();
        Queue<Tuple> queue = new LinkedList<>();
        queue.offer(new Tuple(root, 0, 0));

        while (!queue.isEmpty()) {
            Tuple curr = queue.poll();
            int col = curr.col, row = curr.row;
            TreeNode node = curr.node;

            map.putIfAbsent(col, new ArrayList<>());
            map.get(col).add(new int[]{row, node.val});

            if (node.left != null) queue.offer(new Tuple(node.left, col - 1, row + 1));
            if (node.right != null) queue.offer(new Tuple(node.right, col + 1, row + 1));
        }

        List<List<Integer>> result = new ArrayList<>();
        for (List<int[]> values : map.values()) {
            values.sort(Comparator.comparingInt(a -> a[0]));
            
            List<Integer> sortedList = new ArrayList<>();
            for (int[] val : values) sortedList.add(val[1]);
            result.add(sortedList);
        }
        return result;
    }

    static class Tuple {
        TreeNode node;
        int col;
        int row;
        Tuple(TreeNode node, int col, int row) {
            this.node = node;
            this.col = col;
            this.row = row;
        }
    }
}