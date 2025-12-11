class Solution {
    public boolean parseBoolExpr(String expression) {
        Stack<Character> stack = new Stack<>();
        
        for (char c : expression.toCharArray()) {
            if (c == ',') {
                continue; 
                } else if (c != ')') {
                    stack.push(c);
                }else{
                    Set<Character> seen = new HashSet<>();
                    while (stack.peek() != '(') {
                        seen.add(stack.pop());
                    }
                    stack.pop();
                    char operator = stack.pop();
                    if (operator == '!') {
                        stack.push(seen.contains('t') ? 'f' : 't');
                    } else if (operator == '&') {
                        stack.push(seen.contains('f') ? 'f' : 't');
                    } else if (operator == '|') {
                        stack.push(seen.contains('t') ? 't' : 'f');
                    }
                }
        }
        return stack.pop() == 't';
    }
}