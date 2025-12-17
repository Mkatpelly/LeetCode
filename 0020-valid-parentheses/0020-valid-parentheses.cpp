class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        unordered_map<char, char> bracketMap = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for (char ch : s) {
            // If it’s a closing bracket
            if (bracketMap.count(ch)) {
                if (stk.empty() || stk.top() != bracketMap[ch]) {
                    return false;
                }
                stk.pop(); // matched opening bracket
            } else {
                stk.push(ch); // opening bracket
            }
        }

        return stk.empty();
    }
};