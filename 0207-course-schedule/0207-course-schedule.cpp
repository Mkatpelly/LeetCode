class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Build adjacency list
        vector<vector<int>> adj(numCourses);
        for (auto& pre : prerequisites) {
            adj[pre[1]].push_back(pre[0]);
        }

        // 0=unvisited, 1=visiting, 2=visited
        vector<int> visited(numCourses, 0);

        // DFS function
        function<bool(int)> dfs = [&](int node) {
            if (visited[node] == 1) return false; // cycle
            if (visited[node] == 2) return true;  // already processed

            visited[node] = 1; // mark as visiting
            for (int nei : adj[node]) {
                if (!dfs(nei)) return false;
            }
            visited[node] = 2; // mark as processed
            return true;
        };

        // Check all courses
        for (int i = 0; i < numCourses; ++i) {
            if (!dfs(i)) return false;
        }
        return true;
    }
};
