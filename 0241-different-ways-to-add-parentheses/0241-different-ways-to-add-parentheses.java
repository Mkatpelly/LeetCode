class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        Map<String, List<Integer>> memo = new HashMap<>();
        return compute(expression, memo);
    }
    private List<Integer> compute(String expression, Map<String, List<Integer>> memo) {
        if (memo.containsKey(expression)) {
            return memo.get(expression);
        }

        List<Integer> results = new ArrayList<>();
        if (!expression.contains("+") && !expression.contains("-") && !expression.contains("*")) {
            results.add(Integer.parseInt(expression));
            memo.put(expression, results);
            return results;
        }
        for (int i = 0; i < expression.length(); i++) {
            char c = expression.charAt(i);

            if (c == '+' || c == '-' || c == '*') {
                String left = expression.substring(0, i);
                String right = expression.substring(i + 1);

                List<Integer> leftResults = compute(left, memo);
                List<Integer> rightResults = compute(right, memo);
                for (int leftValue : leftResults) {
                    for (int rightValue : rightResults) {
                        int result = 0;
                        switch (c) {
                            case '+': result = leftValue + rightValue; break;
                            case '-': result = leftValue - rightValue; break;
                            case '*': result = leftValue * rightValue; break;
                        }
                        results.add(result);
                    }
                }
            }
        }
        memo.put(expression, results);
        return results;
    }

}