#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) return {0}; // Edge case: single node

        // Build the graph
        vector<unordered_set<int>> adj(n);
        for (const auto& edge : edges) {
            int a = edge[0], b = edge[1];
            adj[a].insert(b);
            adj[b].insert(a);
        }

        // Initialize leaves (nodes with one neighbor)
        vector<int> leaves;
        for (int i = 0; i < n; ++i) {
            if (adj[i].size() == 1) {
                leaves.push_back(i);
            }
        }

        // Trim leaves layer by layer
        int remaining = n;
        while (remaining > 2) {
            remaining -= leaves.size();
            vector<int> newLeaves;

            for (int leaf : leaves) {
                int neighbor = *adj[leaf].begin(); // Only one neighbor
                adj[neighbor].erase(leaf);
                if (adj[neighbor].size() == 1) {
                    newLeaves.push_back(neighbor);
                }
            }

            leaves = newLeaves;
        }

        return leaves; // Remaining 1 or 2 nodes are MHT roots
    }
};

