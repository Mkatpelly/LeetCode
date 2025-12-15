class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || s.length() <= numRows) return s;

        vector<string> rows(min(numRows, int(s.length())));
        int row = 0;
        bool goingDown = false;

        for (char c : s) {
            rows[row] += c; // Add character to current row
            if (row == 0 || row == numRows - 1) goingDown = !goingDown; // Change direction
            row += goingDown ? 1 : -1; // Move up or down
        }

        string result;
        for (string r : rows) result += r; // Combine rows

        return result;
    }
};