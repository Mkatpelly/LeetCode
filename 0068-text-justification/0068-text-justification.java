class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int n = words.length;
        int index = 0;
        while (index < n){
            int totalChars = words[index].length();
            int last = index + 1;
            while (last < n && totalChars + 1 + words[last].length() <= maxWidth) {
                totalChars += 1 + words[last].length();
                last++;
            }
            StringBuilder line = new StringBuilder();
            int numberOfWords = last - index;
            int spaces = maxWidth - totalChars + (numberOfWords - 1);
            if (last == n || numberOfWords == 1) {
                for (int i = index; i < last; i++) {
                    line.append(words[i]);
                    if (i < last - 1) {
                        line.append(" ");
                    }
                }
                while (line.length() < maxWidth) {
                    line.append(" ");
                }
            } else {
                int spaceBetweenWords = spaces / (numberOfWords - 1);
                int extraSpaces = spaces % (numberOfWords - 1);

                for (int i = index; i < last - 1; i++) {
                    line.append(words[i]);
                    line.append(" ".repeat(spaceBetweenWords));
                    if (extraSpaces > 0) {
                        line.append(" ");
                        extraSpaces--;
                    }
                }
                line.append(words[last - 1]); // Append the last word
            }

            result.add(line.toString());
            index = last;
        }

        return result;
        
    }
}