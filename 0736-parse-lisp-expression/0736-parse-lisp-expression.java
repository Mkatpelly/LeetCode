class Solution {
    public int evaluate(String expression) {
        return evaluate(expression, new HashMap<>());
    }
    private static String[] splitExpression(String expression) {
        List<String> tokens = new ArrayList<>();
        int balance = 0;
        StringBuilder sb = new StringBuilder();

        for (char c : expression.toCharArray()) {
            if (c == '(') {
                balance++;
            } else if (c == ')') {
                balance--;
            }
            if (c == ' ' && balance == 0) {
                tokens.add(sb.toString());
                sb.setLength(0);
            } else {
                sb.append(c);
            }
        }
        tokens.add(sb.toString());
        return tokens.toArray(new String[0]);
    }
    private static int evaluate(String expression, Map<String, Integer> scope){
        if (expression.charAt(0) != '(') {
            if (Character.isDigit(expression.charAt(0)) || expression.charAt(0) == '-') {
                return Integer.parseInt(expression);
            } else {
                return scope.get(expression);
            }
        }
        String stripped = expression.substring(1, expression.length() - 1);
        String[] tokens = splitExpression(stripped);

        if (tokens[0].equals("add")) {
            return evaluate(tokens[1], scope) + evaluate(tokens[2], scope);
        } else if (tokens[0].equals("mult")) {
            return evaluate(tokens[1], scope) * evaluate(tokens[2], scope);
        } else {
            
            Map<String, Integer> newScope = new HashMap<>(scope);
            for (int i = 1; i < tokens.length - 1; i += 2) {
                newScope.put(tokens[i], evaluate(tokens[i + 1], newScope));
            }
            return evaluate(tokens[tokens.length - 1], newScope);
        }
    }
}