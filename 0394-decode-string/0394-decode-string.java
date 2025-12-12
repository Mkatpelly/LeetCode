class Solution {
    public String decodeString(String s) {
        Stack<String> stack = new Stack<>();
        StringBuilder currentString = new StringBuilder();
        int currentNum = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                currentNum = currentNum * 10 + (c - '0');
            } else if (c == '[') {
                stack.push(currentString.toString());
                stack.push(String.valueOf(currentNum));
                currentString = new StringBuilder();
                currentNum = 0;
            } else if (c == ']') {
                int repeatCount = Integer.parseInt(stack.pop());
                String previousString = stack.pop();
                for (int i = 0; i < repeatCount; i++) {
                    previousString += currentString.toString();
                }
                currentString = new StringBuilder(previousString);
            } else {
                currentString.append(c);
            }
        }

        return currentString.toString();
    }
}