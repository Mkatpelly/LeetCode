class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), k, n, 1);
        return res;
    }
    private void backtrack(List<List<Integer>> res, List<Integer> comb, int k, int remain, int start) {
        if (comb.size() == k && remain == 0) {
            res.add(new ArrayList<>(comb));
            return;
        }
        if (comb.size() > k || remain < 0) return;
        for (int i = start; i <= 9; i++) {
            comb.add(i);
            backtrack(res, comb, k, remain - i, i + 1);
            comb.remove(comb.size() - 1);
        }
    }
}