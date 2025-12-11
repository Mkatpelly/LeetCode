class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits == null || digits.isEmpty()) return new ArrayList<>();
        
        // Mapping of digits to letters
        Map<Character, String> phoneMap = Map.of(
            '2', "abc", '3', "def", '4', "ghi", '5', "jkl",
            '6', "mno", '7', "pqrs", '8', "tuv", '9', "wxyz"
        );

        List<String> result = new ArrayList<>();
        backtrack(result, digits, phoneMap, new StringBuilder(), 0);
        return result;
    }

    private static void backtrack(List<String> result, String digits, Map<Character, String> phoneMap, StringBuilder path, int index) {
        if (index == digits.length()) {
            result.add(path.toString());
            return;
        }
        
        String letters = phoneMap.get(digits.charAt(index));
        for (char letter : letters.toCharArray()) {
            path.append(letter);  // Choose
            backtrack(result, digits, phoneMap, path, index + 1);  // Explore
            path.deleteCharAt(path.length() - 1);  // Un-choose (Backtrack)
        }
    }
    }
