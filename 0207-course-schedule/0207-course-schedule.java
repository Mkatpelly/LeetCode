class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] pre : prerequisites) {
            graph.get(pre[1]).add(pre[0]);
        }
        int[] visited = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (dfs(i, graph, visited)) return false;
        }
        return true;

    }
     private boolean dfs(int course, List<List<Integer>> graph, int[] visited){
        if (visited[course] == 1) return true;
        if (visited[course] == 2) return false;
        visited[course] = 1;
        for (int neighbor : graph.get(course)) {
            if (dfs(neighbor, graph, visited)) return true;
        }
        visited[course] = 2;
        return false;
     }
}