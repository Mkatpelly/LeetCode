#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> cnt(26, 0);
        int left = 0;
        int maxFreq = 0;   // max count of a single letter in current window
        int best = 0;

        for (int right = 0; right < (int)s.size(); right++) {
            int idx = s[right] - 'A';
            cnt[idx]++;
            maxFreq = max(maxFreq, cnt[idx]);

            // If we need more than k replacements, shrink from left
            while ((right - left + 1) - maxFreq > k) {
                cnt[s[left] - 'A']--;
                left++;
                // Note: we don't necessarily recompute maxFreq here; it's okay.
            }

            best = max(best, right - left + 1);
        }
        return best;
    }
};
