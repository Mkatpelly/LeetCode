class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        return backtrack(s, wordSet, 0, new ArrayList<>(), new ArrayList<>());
    }
    private List<String> backtrack(String s, Set<String> wordSet, int start, List<String> path, List<String> result) {
        if (start == s.length()) {
            result.add(String.join(" ", path));
            return result;
        }

        for (int end = start + 1; end <= s.length(); end++) {
            String word = s.substring(start, end);
            if (wordSet.contains(word)) {
                path.add(word);
                backtrack(s, wordSet, end, path, result);
                path.remove(path.size() - 1);
            }
        }

        return result;
    }
}