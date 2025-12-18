class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> result;
        if (words.empty() || s.empty()) return result;

        int word_len = words[0].length();
        int word_count = words.size();
        int total_len = word_len * word_count;
        int s_len = s.length();

        if (s_len < total_len) return result;

        unordered_map<string, int> word_map;
        for (const string& word : words) {
            word_map[word]++;
        }

        // Try every possible offset within a word_len
        for (int i = 0; i < word_len; i++) {
            int left = i, right = i, count = 0;
            unordered_map<string, int> window_map;

            while (right + word_len <= s_len) {
                string word = s.substr(right, word_len);
                right += word_len;

                if (word_map.count(word)) {
                    window_map[word]++;
                    count++;

                    // If there are more occurrences than allowed, shrink the window
                    while (window_map[word] > word_map[word]) {
                        string left_word = s.substr(left, word_len);
                        window_map[left_word]--;
                        left += word_len;
                        count--;
                    }

                    if (count == word_count) {
                        result.push_back(left);
                    }
                } else {
                    // Invalid word, reset
                    window_map.clear();
                    count = 0;
                    left = right;
                }
            }
        }

        return result;
    }
};
