class Solution {
    public String minWindow(String s, String t) {
        if (s == null || s.length() == 0 || t == null || t.length() == 0) {
            return "";
        }
    HashMap<Character, Integer> tMap = new HashMap<>();
        for (char c : t.toCharArray()) {
            tMap.put(c, tMap.getOrDefault(c, 0) + 1);
        }
    int required = tMap.size();
    int left = 0, right = 0;
    int formed = 0;
    HashMap<Character, Integer> windowCounts = new HashMap<>();
    int[] result = {-1, 0, 0};
    while (right < s.length()) {
            char c = s.charAt(right);
            windowCounts.put(c, windowCounts.getOrDefault(c, 0) + 1);
            if (tMap.containsKey(c) && windowCounts.get(c).intValue() == tMap.get(c).intValue()) {
                formed++;
            }
            while (left <= right && formed == required) {
                c = s.charAt(left);
            if (result[0] == -1 || right - left + 1 < result[0]) {
                    result[0] = right - left + 1;
                    result[1] = left;
                    result[2] = right;
                }
                windowCounts.put(c, windowCounts.get(c) - 1);
                if (tMap.containsKey(c) && windowCounts.get(c).intValue() < tMap.get(c).intValue()) {
                    formed--;
                }

                left++;
            }
            right++;

    }
    return result[0] == -1 ? "" : s.substring(result[1], result[2] + 1);
}
}