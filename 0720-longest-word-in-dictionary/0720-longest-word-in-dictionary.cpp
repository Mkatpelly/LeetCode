#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end(), [](const string& a, const string& b) {
            if (a.size() != b.size()) return a.size() < b.size();
            return a < b;
        });

        unordered_set<string> ok;
        string best = "";

        for (const string& w : words) {
            if (w.size() == 1 || ok.count(w.substr(0, w.size() - 1))) {
                ok.insert(w);

                if (w.size() > best.size() || (w.size() == best.size() && w < best)) {
                    best = w;
                }
            }
        }
        return best;
    }
};
