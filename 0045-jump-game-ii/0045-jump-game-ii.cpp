#include <vector>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int jumps = 0, farthest = 0, end = 0;

        // We do not need to jump from the last index
        for (int i = 0; i < n - 1; ++i) {
            farthest = max(farthest, i + nums[i]);

            // If we've reached the end of the current jump
            if (i == end) {
                jumps++;
                end = farthest;
            }
        }

        return jumps;
    }
};
