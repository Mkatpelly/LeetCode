#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> leftmostBuildingQueries(vector<int>& heights, vector<vector<int>>& queries) {
        int n = (int)heights.size();
        int m = (int)queries.size();
        vector<int> ans(m, -1);

        // start[pos] holds queries that begin searching at index pos
        // each item: (threshold, queryIndex)
        vector<vector<pair<int,int>>> start(n);

        for (int qi = 0; qi < m; qi++) {
            int a = queries[qi][0];
            int b = queries[qi][1];

            if (a == b) {
                ans[qi] = a;
                continue;
            }

            if (a > b) swap(a, b); // ensure a < b

            if (heights[a] < heights[b]) {
                // Alice can go directly to b, and b is the leftmost meeting spot.
                ans[qi] = b;
                continue;
            }

            // Need some j > b with heights[j] > heights[a]
            int pos = b + 1;
            if (pos < n) {
                start[pos].push_back({heights[a], qi});
            }
            // else remains -1
        }

        // min-heap by threshold
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

        for (int i = 0; i < n; i++) {
            for (auto &p : start[i]) pq.push(p);

            while (!pq.empty() && pq.top().first < heights[i]) {
                ans[pq.top().second] = i;
                pq.pop();
            }
        }

        return ans;
    }
};
