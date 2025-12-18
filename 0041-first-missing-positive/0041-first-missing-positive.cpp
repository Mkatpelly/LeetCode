#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = (int)nums.size();

        // Place each number x in position x-1 if 1 <= x <= n
        for (int i = 0; i < n; i++) {
            while (nums[i] >= 1 && nums[i] <= n) {
                int correct = nums[i] - 1;
                if (nums[i] == nums[correct]) break; // avoid infinite loop on duplicates
                swap(nums[i], nums[correct]);
            }
        }

        // Find first place where index doesn't match value
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) return i + 1;
        }

        return n + 1;
    }
};
