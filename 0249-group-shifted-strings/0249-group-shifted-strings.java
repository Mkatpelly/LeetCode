class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        Map<String, List<String>> map = new HashMap<>();
        
        for (String s : strings) {
            String baseForm = normalize(s);
            map.putIfAbsent(baseForm, new ArrayList<>());
            map.get(baseForm).add(s);
        }

        return new ArrayList<>(map.values());
    }
    private static String normalize(String s) {
        char[] chars = s.toCharArray();
        int shift = chars[0] - 'a';

        for (int i = 0; i < chars.length; i++) {
            chars[i] = (char) ((chars[i] - shift + 26) % 26 + 'a');
        }

        return new String(chars);
    }
}