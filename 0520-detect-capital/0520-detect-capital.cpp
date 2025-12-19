#include <string>
using namespace std;

class Solution {
public:
    bool detectCapitalUse(string word) {
        int caps = 0;
        for (char c : word) {
            if (isupper(c)) caps++;
        }

        if (caps == word.size()) return true;              // ALL caps
        if (caps == 0) return true;                         // all lowercase
        if (caps == 1 && isupper(word[0])) return true;     // first only

        return false;
    }
};
