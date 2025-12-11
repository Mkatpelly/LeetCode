class Solution {
    public int shortestWordDistance(String[] wordsDict, String word1, String word2) {
        int idx1 = -1, idx2 = -1;
        int minDist = wordsDict.length;
        boolean same = word1.equals(word2);

        for (int i = 0; i < wordsDict.length; i++) {
            String word = wordsDict[i];
            if (same) {
                if (word.equals(word1)) {
                    if (idx1 != -1) {
                        minDist = Math.min(minDist, i - idx1);
                    }
                    idx1 = i;
                }
            } else {
                if (word.equals(word1)) {
                    idx1 = i;
                    if (idx2 != -1) {
                        minDist = Math.min(minDist, Math.abs(idx1 - idx2));
                    }
                } else if (word.equals(word2)) {
                    idx2 = i;
                    if (idx1 != -1) {
                        minDist = Math.min(minDist, Math.abs(idx1 - idx2));
                    }
                }
            }
        }
        return minDist;
    }
}