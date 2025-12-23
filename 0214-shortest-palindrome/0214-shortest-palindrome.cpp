#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string shortestPalindrome(string s) {
        int n = (int)s.size();
        if (n <= 1) return s;

        string rev = s;
        reverse(rev.begin(), rev.end());

        string temp = s + "#" + rev;  // '#' is a separator not in lowercase letters
        vector<int> pi(temp.size(), 0);

        for (int i = 1; i < (int)temp.size(); i++) {
            int j = pi[i - 1];
            while (j > 0 && temp[i] != temp[j]) j = pi[j - 1];
            if (temp[i] == temp[j]) j++;
            pi[i] = j;
        }

        int L = pi.back();                 // longest palindromic prefix length
        string add = s.substr(L);          // part not in that prefix
        reverse(add.begin(), add.end());   // add reversed to front
        return add + s;
    }
};

