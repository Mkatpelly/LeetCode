class Solution {
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        int currentNumber = 0;
        char currentOperation = '+';
        s = s.replaceAll(" ", ""); // Remove any spaces
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            
            if (Character.isDigit(ch)) {
                currentNumber = currentNumber * 10 + (ch - '0');
            }
            
            if (ch == '(') {
                // Handle sub-expression within parentheses
                int j = i, braces = 0;
                for (; i < s.length(); i++) {
                    if (s.charAt(i) == '(') braces++;
                    if (s.charAt(i) == ')') braces--;
                    if (braces == 0) break;
                }
                currentNumber = calculate(s.substring(j + 1, i));
            }
            
            if (!Character.isDigit(ch) || i == s.length() - 1) {
                switch (currentOperation) {
                    case '+':
                        stack.push(currentNumber);
                        break;
                    case '-':
                        stack.push(-currentNumber);
                        break;
                    case '*':
                        stack.push(stack.pop() * currentNumber);
                        break;
                    case '/':
                        stack.push(stack.pop() / currentNumber);
                        break;
                }
                currentOperation = ch;
                currentNumber = 0;
            }
        }
        
        int result = 0;
        while (!stack.isEmpty()) {
            result += stack.pop();
        }
        
        return result;
    }
}