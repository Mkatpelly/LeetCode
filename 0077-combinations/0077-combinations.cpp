#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> result;
    vector<int> curr;

    void backtrack(int start, int n, int k) {
        if (curr.size() == k) {
            result.push_back(curr);
            return;
        }

        for (int i = start; i <= n; i++) {
            curr.push_back(i);
            backtrack(i + 1, n, k);
            curr.pop_back(); // undo choice
        }
    }

    vector<vector<int>> combine(int n, int k) {
        backtrack(1, n, k);
        return result;
    }
};
