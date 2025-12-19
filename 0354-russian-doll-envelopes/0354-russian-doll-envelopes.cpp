class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        // Sort by increasing width and decreasing height
        sort(envelopes.begin(), envelopes.end(), [](const vector<int>& a, const vector<int>& b){
            if (a[0] == b[0])
                return b[1] < a[1];
            return a[0] < b[0];
        });

        // Extract heights
        vector<int> heights;
        for (auto& env : envelopes) {
            heights.push_back(env[1]);
        }

        // Find LIS of heights
        vector<int> dp;
        for (int h : heights) {
            auto it = lower_bound(dp.begin(), dp.end(), h);
            if (it == dp.end()) {
                dp.push_back(h);
            } else {
                *it = h;
            }
        }

        return dp.size();
    }
};
