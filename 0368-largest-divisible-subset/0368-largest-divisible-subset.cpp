class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        if (nums.empty()) return {};
        int n = nums.size();
        sort(nums.begin(), nums.end());
        
        vector<int> dp(n, 1);      // dp[i] = max subset length ending at i
        vector<int> prev(n, -1);   // to reconstruct the subset
        
        int max_idx = 0;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
            if (dp[i] > dp[max_idx]) {
                max_idx = i;
            }
        }
        
        // Reconstruct the subset
        vector<int> res;
        for (int k = max_idx; k >= 0; k = prev[k]) {
            res.push_back(nums[k]);
            if (prev[k] == -1) break;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
