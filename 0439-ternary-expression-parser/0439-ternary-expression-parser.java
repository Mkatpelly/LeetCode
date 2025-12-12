class Solution {
    public String parseTernary(String expression) {
        Deque<Character> stack = new ArrayDeque<>();
        
        for (int i = expression.length() - 1; i >= 0; i--) {
            char ch = expression.charAt(i);

            if (!stack.isEmpty() && stack.peek() == '?') {
                stack.pop(); // Remove '?'
                char trueExpr = stack.pop();
                stack.pop(); // Remove ':'
                char falseExpr = stack.pop();
                
                if (ch == 'T') {
                    stack.push(trueExpr);
                } else {
                    stack.push(falseExpr);
                }
            } else {
                stack.push(ch);
            }
        }
        return String.valueOf(stack.peek());
    }
}