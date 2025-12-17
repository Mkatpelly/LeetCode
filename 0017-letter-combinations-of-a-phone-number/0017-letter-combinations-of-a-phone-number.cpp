class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> phoneMap = {
            "",     "",     "abc",  "def", "ghi", 
            "jkl",  "mno",  "pqrs", "tuv", "wxyz"
        };

        vector<string> result;
        string current;

        backtrack(digits, 0, current, phoneMap, result);
        return result;
    }
    private:
    void backtrack(const string& digits, int index, string& current, 
                   const vector<string>& phoneMap, vector<string>& result) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }

        string letters = phoneMap[digits[index] - '0'];
        for (char letter : letters) {
            current.push_back(letter);
            backtrack(digits, index + 1, current, phoneMap, result);
            current.pop_back(); // backtrack
        }
    }

};