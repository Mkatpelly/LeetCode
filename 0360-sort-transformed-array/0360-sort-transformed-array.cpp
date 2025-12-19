class Solution {
public:
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        int n = nums.size();
        vector<int> res(n);
        int i = 0, j = n - 1;
        int idx = (a >= 0) ? n - 1 : 0;
        
        auto quad = [&](int x) {
            return a * x * x + b * x + c;
        };
        
        while (i <= j) {
            int left = quad(nums[i]);
            int right = quad(nums[j]);
            if (a >= 0) {
                if (left > right) {
                    res[idx--] = left;
                    i++;
                } else {
                    res[idx--] = right;
                    j--;
                }
            } else {
                if (left < right) {
                    res[idx++] = left;
                    i++;
                } else {
                    res[idx++] = right;
                    j--;
                }
            }
        }
        
        return res;
    }
};
