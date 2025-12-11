class Solution {
    static class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        String word = null;
    }

    private TrieNode root = new TrieNode();
    private Set<String> result = new HashSet<>();
    private int m, n;
    private char[][] board;

    public List<String> findWords(char[][] board, String[] words) {
        this.board = board;
        m = board.length;
        n = board[0].length;
        for (String word : words) insert(word);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (root.children.containsKey(board[i][j])) {
                    backtrack(i, j, root);
                }
            }
        }
        return new ArrayList<>(result);
    }
    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.word = word;
    }
    private void backtrack(int i, int j, TrieNode node){
        char c = board[i][j];
        if (!node.children.containsKey(c)) return;

        TrieNode nextNode = node.children.get(c);
        if (nextNode.word != null) {
            result.add(nextNode.word);
            nextNode.word = null;
        }
        board[i][j] = '#';
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (int[] d : directions) {
            int x = i + d[0], y = j + d[1];
            if (x >= 0 && x < m && y >= 0 && y < n) {
                backtrack(x, y, nextNode);
            }
        }
        board[i][j] = c;
        if (nextNode.children.isEmpty()) {
            node.children.remove(c);
        }
    }

}