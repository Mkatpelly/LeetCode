class Solution {
public:
    char kthBit(int n, int k) {
        if (n == 1) return '0';

        int mid = 1 << (n - 1);      // 2^(n-1)
        int len = (1 << n) - 1;      // 2^n - 1

        if (k == mid) return '1';
        if (k < mid) return kthBit(n - 1, k);

        // mirror and invert
        char c = kthBit(n - 1, len - k + 1);
        return (c == '0') ? '1' : '0';
    }

    char findKthBit(int n, int k) {
        return kthBit(n, k);
    }
};
