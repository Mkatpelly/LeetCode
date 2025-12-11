class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> result = new ArrayList<>();
        backtrack(result, num, target, "", 0, 0, 0);
        return result;
    }

    private static void backtrack(List<String> result, String num, int target, String path, int index, long eval, long multed){
        if (index == num.length()) {
            if (eval == target) {
                result.add(path);
            }
            return;
        }
        for (int i = index; i < num.length(); i++) {
            if (i != index && num.charAt(index) == '0') {
                break;
                }
            long curr = Long.parseLong(num.substring(index, i + 1));
            if (index == 0) {
                 backtrack(result, num, target, path + curr, i + 1, curr, curr);
            } else {
                backtrack(result, num, target, path + "+" + curr, i + 1, eval + curr, curr);
                backtrack(result, num, target, path + "-" + curr, i + 1, eval - curr, -curr);
                backtrack(result, num, target, path + "*" + curr, i + 1, eval - multed + multed * curr, multed * curr);
            }
        }
    }
}