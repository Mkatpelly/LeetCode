class Solution {
public:
    long long countSteps(long long n, long long prefix, long long nextPrefix) {
        long long steps = 0;
        while (prefix <= n) {
            steps += min(n + 1, nextPrefix) - prefix;
            prefix *= 10;
            nextPrefix *= 10;
        }
        return steps;
    }

    int findKthNumber(int n, int k) {
        long long cur = 1;
        k--; // we are already at 1

        while (k > 0) {
            long long steps = countSteps(n, cur, cur + 1);
            if (steps <= k) {
                // skip this whole prefix subtree
                cur++;
                k -= (int)steps;
            } else {
                // go deeper into this prefix subtree
                cur *= 10;
                k--;
            }
        }
        return (int)cur;
    }
};
