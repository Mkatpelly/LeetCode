class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEndOfWord;
}
class Trie {
    TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index];
        }
        node.isEndOfWord = true;
    }

    public boolean search(String word, int start, TrieNode node) {
        if (start == word.length()) return true;
        TrieNode current = node;
        for (int i = start; i < word.length(); i++) {
            int index = word.charAt(i) - 'a';
            if (current.children[index] == null) return false;
            current = current.children[index];
            if (current.isEndOfWord && search(word, i + 1, node)) {
                return true;
            }
        }
        return false;
    }
}

class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> result = new ArrayList<>();
        if (words == null || words.length == 0) return result;

        Trie trie = new Trie();
        Arrays.sort(words, (a, b) -> a.length() - b.length());

        for (String word : words) {
            if (word.length() == 0) continue;
            if (trie.search(word, 0, trie.root)) {
                result.add(word);
            } else {
                trie.insert(word);
            }
        }

        return result;
    }
}