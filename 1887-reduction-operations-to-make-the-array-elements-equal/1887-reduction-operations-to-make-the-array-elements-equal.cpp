#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        long long ops = 0;  // use long long to be safe for large n

        // Walk from right to left, skipping index 0
        for (int i = n - 1; i > 0; --i) {
            if (nums[i] != nums[i - 1]) {
                // nums[i] starts a new larger value block
                // all elements from i to n-1 need to be reduced at this level
                ops += (n - i);
            }
        }

        return (int)ops;
    }
};
