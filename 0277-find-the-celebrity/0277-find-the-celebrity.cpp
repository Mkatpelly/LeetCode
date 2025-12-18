// Provided knows(a, b) API
bool knows(int a, int b);  // You should implement this in test scaffolding

class Solution {
public:
    int findCelebrity(int n) {
        int candidate = 0;

        // Step 1: Find potential candidate
        for (int i = 1; i < n; ++i) {
            if (knows(candidate, i)) {
                candidate = i;  // candidate cannot be celebrity
            }
            // else i cannot be celebrity, candidate stays
        }

        // Step 2: Validate candidate
        for (int i = 0; i < n; ++i) {
            if (i == candidate) continue;
            // Candidate should not know i, and i should know candidate
            if (knows(candidate, i) || !knows(i, candidate)) {
                return -1;
            }
        }

        return candidate;
    }
};
