class Solution {
    private Map<String, Map<String, Double>> graph = new HashMap<>();
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        for (int i = 0; i < equations.size(); i++) {
            String A = equations.get(i).get(0);
            String B = equations.get(i).get(1);
            double value = values[i];

            graph.putIfAbsent(A, new HashMap<>());
            graph.putIfAbsent(B, new HashMap<>());
            graph.get(A).put(B, value);
            graph.get(B).put(A, 1 / value);
        }
        double[] results = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            String C = queries.get(i).get(0);
            String D = queries.get(i).get(1);
            results[i] = dfs(C, D, new HashSet<>());
        }
        return results;
    }
    private double dfs(String current, String target, Set<String> visited) {
        if (!graph.containsKey(current) || !graph.containsKey(target)) return -1.0;
        if (current.equals(target)) return 1.0;

        visited.add(current);
        for (Map.Entry<String, Double> neighbor : graph.get(current).entrySet()) {
            if (!visited.contains(neighbor.getKey())) {
                double product = dfs(neighbor.getKey(), target, visited);
                if (product != -1.0) {
                    return product * neighbor.getValue();
                }
            }
        }
        return -1.0;
    }
}