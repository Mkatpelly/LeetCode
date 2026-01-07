class NumArray {
private:
    int n;
    vector<int> bit;
    vector<int> nums;

    // Add delta to index i
    void add(int i, int delta) {
        i++; // Fenwick Tree is 1-indexed
        while (i <= n) {
            bit[i] += delta;
            i += i & -i;
        }
    }

    // Prefix sum from 0 to i
    int prefixSum(int i) {
        i++;
        int sum = 0;
        while (i > 0) {
            sum += bit[i];
            i -= i & -i;
        }
        return sum;
    }

public:
    NumArray(vector<int>& nums) {
        this->nums = nums;
        n = nums.size();
        bit.assign(n + 1, 0);

        // Build Fenwick Tree
        for (int i = 0; i < n; i++) {
            add(i, nums[i]);
        }
    }

    void update(int index, int val) {
        int delta = val - nums[index];
        nums[index] = val;
        add(index, delta);
    }

    int sumRange(int left, int right) {
        return prefixSum(right) - prefixSum(left - 1);
    }
};
