class WordDistance {
    private Map<String, List<Integer>> map;

    public WordDistance(String[] wordsDict) {
        map = new HashMap<>();
        for (int i = 0; i < wordsDict.length; i++) {
            map.computeIfAbsent(wordsDict[i], k -> new ArrayList<>()).add(i);
        }
    }
    
    public int shortest(String word1, String word2) {
        List<Integer> list1 = map.get(word1);
        List<Integer> list2 = map.get(word2);
        int i = 0, j = 0, minDist = Integer.MAX_VALUE;
        // Two pointer technique
        while (i < list1.size() && j < list2.size()) {
            int pos1 = list1.get(i), pos2 = list2.get(j);
            minDist = Math.min(minDist, Math.abs(pos1 - pos2));
            if (pos1 < pos2) i++;
            else j++;
        }
        return minDist;
    }
}

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance obj = new WordDistance(wordsDict);
 * int param_1 = obj.shortest(word1,word2);
 */