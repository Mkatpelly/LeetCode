#include <vector>
using namespace std;

class Solution {
public:
    vector<int> beautifulArray(int n) {
        vector<int> res = {1};

        // Iteratively build up a beautiful array for [1..n]
        while ((int)res.size() < n) {
            vector<int> tmp;
            // First, make all odds: 2*x - 1
            for (int x : res) {
                int val = 2 * x - 1;
                if (val <= n) tmp.push_back(val);
            }
            // Then, make all evens: 2*x
            for (int x : res) {
                int val = 2 * x;
                if (val <= n) tmp.push_back(val);
            }
            res.swap(tmp);
        }

        return res;
    }
};

