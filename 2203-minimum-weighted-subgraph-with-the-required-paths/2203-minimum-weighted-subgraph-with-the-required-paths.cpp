#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    using ll = long long;
    static constexpr ll INF = (1LL<<62);

    vector<ll> dijkstra(int n, vector<vector<pair<int,int>>>& g, int src) {
        vector<ll> dist(n, INF);
        priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;

        dist[src] = 0;
        pq.push({0, src});

        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d != dist[u]) continue;
            for (auto [v, w] : g[u]) {
                ll nd = d + (ll)w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.push({nd, v});
                }
            }
        }
        return dist;
    }

    long long minimumWeight(int n, vector<vector<int>>& edges,
                            int src1, int src2, int dest) {
        vector<vector<pair<int,int>>> g(n), rg(n); // rg = reversed graph
        g.reserve(n); rg.reserve(n);

        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            rg[v].push_back({u, w});
        }

        vector<ll> d1 = dijkstra(n, g, src1);
        vector<ll> d2 = dijkstra(n, g, src2);
        vector<ll> dd = dijkstra(n, rg, dest); // distance to dest

        ll ans = INF;
        for (int x = 0; x < n; x++) {
            if (d1[x] == INF || d2[x] == INF || dd[x] == INF) continue;
            ans = min(ans, d1[x] + d2[x] + dd[x]);
        }

        return (ans == INF) ? -1 : ans;
    }
};
