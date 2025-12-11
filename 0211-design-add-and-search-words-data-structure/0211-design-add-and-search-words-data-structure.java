class TrieNode {
    Map<Character, TrieNode> children;
    boolean isEndOfWord;

    public TrieNode() {
        children = new HashMap<>();
        isEndOfWord = false;
    }
}
class WordDictionary {
    private TrieNode root;
    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            node.children.putIfAbsent(ch, new TrieNode());
            node = node.children.get(ch);
        }
        node.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        return dfsSearch(word, 0, root);
    }
    private boolean dfsSearch(String word, int index, TrieNode node) {
        if (index == word.length()) return node.isEndOfWord;

        char ch = word.charAt(index);
        if (ch == '.') {
            for (TrieNode child : node.children.values()) {
                if (dfsSearch(word, index + 1, child)) return true;
            }
            return false;
        } else {
            if (!node.children.containsKey(ch)) return false;
            return dfsSearch(word, index + 1, node.children.get(ch));
        }
    }


}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */