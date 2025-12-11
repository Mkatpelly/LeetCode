class Solution {
    public int[][] multiply(int[][] mat1, int[][] mat2) {
        int m = mat1.length;
        int k = mat1[0].length;
        int n = mat2[0].length;
        Map<Integer, Map<Integer, Integer>> mat1NonZero = new HashMap<>();
        Map<Integer, Map<Integer, Integer>> mat2NonZero = new HashMap<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < k; j++) {
                if (mat1[i][j] != 0) {
                    mat1NonZero.putIfAbsent(i, new HashMap<>());
                    mat1NonZero.get(i).put(j, mat1[i][j]);
                }
            }
        }
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < n; j++) {
                if (mat2[i][j] != 0) {
                    mat2NonZero.putIfAbsent(i, new HashMap<>());
                    mat2NonZero.get(i).put(j, mat2[i][j]);
                }
            }
        }
        int[][] result = new int[m][n];
        for (int i : mat1NonZero.keySet()) {
            for (int j : mat1NonZero.get(i).keySet()) {
                if (mat2NonZero.containsKey(j)) {
                    for (int l : mat2NonZero.get(j).keySet()) {
                        result[i][l] += mat1NonZero.get(i).get(j) * mat2NonZero.get(j).get(l);
                    }
                }
            }
        }
        
        return result;
    }
}