#include <bits/stdc++.h>
using namespace std;

class Graph {
    static constexpr long long INF = (1LL << 60);
    int n;
    vector<vector<long long>> dist;

public:
    Graph(int n, vector<vector<int>>& edges) : n(n), dist(n, vector<long long>(n, INF)) {
        for (int i = 0; i < n; i++) dist[i][i] = 0;

        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            dist[u][v] = min(dist[u][v], (long long)w);
        }

        // Floyd-Warshall
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (dist[i][k] == INF) continue;
                for (int j = 0; j < n; j++) {
                    if (dist[k][j] == INF) continue;
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    void addEdge(vector<int> edge) {
        int u = edge[0], v = edge[1], w = edge[2];

        if ((long long)w < dist[u][v]) dist[u][v] = w;

        for (int i = 0; i < n; i++) {
            if (dist[i][u] == INF) continue;
            for (int j = 0; j < n; j++) {
                if (dist[v][j] == INF) continue;
                long long cand = dist[i][u] + (long long)w + dist[v][j];
                if (cand < dist[i][j]) dist[i][j] = cand;
            }
        }
    }

    int shortestPath(int node1, int node2) {
        long long d = dist[node1][node2];
        return d == INF ? -1 : (int)d;
    }
};

