class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        for (int num : nums) {
            List<List<Integer>> newResult = new ArrayList<>();

            for (List<Integer> perm : result) {
                for (int i = 0; i <= perm.size(); i++) { 
                    List<Integer> newPerm = new ArrayList<>(perm);
                    newPerm.add(i, num);
                    newResult.add(newPerm);
                }
            }

            result = newResult;
        }
        return result;
    }
}