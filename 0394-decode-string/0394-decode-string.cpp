#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        stack<int> counts;
        stack<string> strs;

        string curr;
        int num = 0;

        for (char c : s) {
            if (isdigit(c)) {
                num = num * 10 + (c - '0');          // build multi-digit k
            } 
            else if (c == '[') {
                counts.push(num);
                strs.push(curr);
                num = 0;
                curr.clear();
            } 
            else if (c == ']') {
                int k = counts.top(); counts.pop();
                string prev = strs.top(); strs.pop();

                string repeated;
                repeated.reserve(curr.size() * k);
                for (int i = 0; i < k; i++) repeated += curr;

                curr = prev + repeated;
            } 
            else { // letter
                curr.push_back(c);
            }
        }

        return curr;
    }
};
