class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        if (mat == null || mat.length == 0 || mat[0].length == 0) {
            return new int[0];
        }

        int m = mat.length;
        int n = mat[0].length;
        List<Integer> result = new ArrayList<>();
        for (int d = 0; d < m + n - 1; d++){
            int row = (d < n) ? 0 : d - n + 1;
            int col = (d < n) ? d : n - 1;
            List<Integer> diagonal = new ArrayList<>();
            while (row < m && col >= 0) {
                diagonal.add(mat[row][col]);
                row++;
                col--;
            }
            if (d % 2 == 0) {
                Collections.reverse(diagonal);
            }
            result.addAll(diagonal);
        }
        int[] resultArray = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            resultArray[i] = result.get(i);
        }
        return resultArray;

    }
}