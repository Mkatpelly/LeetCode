class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> path;
        vector<bool> used(nums.size(), false);

        sort(nums.begin(), nums.end());
        backtrack(nums, used, path, result);
        return result;
    }

private:
    void backtrack(vector<int>& nums, vector<bool>& used, vector<int>& path, vector<vector<int>>& result) {
        if (path.size() == nums.size()) {
            result.push_back(path);
            return;
        }

        for (int i = 0; i < nums.size(); ++i) {
            // Skip already used
            if (used[i]) continue;

            // Skip duplicates
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;

            // Choose
            used[i] = true;
            path.push_back(nums[i]);

            // Explore
            backtrack(nums, used, path, result);

            // Un-choose
            path.pop_back();
            used[i] = false;
        }
    }
};
