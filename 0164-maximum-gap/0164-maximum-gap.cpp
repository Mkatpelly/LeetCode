class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;
        
        int minVal = *min_element(nums.begin(), nums.end());
        int maxVal = *max_element(nums.begin(), nums.end());

        if (minVal == maxVal) return 0; // all numbers are equal

        // Compute bucket size and number of buckets
        int bucketSize = max(1, (maxVal - minVal) / (n - 1));
        int bucketCount = (maxVal - minVal) / bucketSize + 1;

        vector<int> bucketMin(bucketCount, INT_MAX);
        vector<int> bucketMax(bucketCount, INT_MIN);
        vector<bool> bucketUsed(bucketCount, false);

        // Place numbers into buckets
        for (int num : nums) {
            int idx = (num - minVal) / bucketSize;
            bucketMin[idx] = min(bucketMin[idx], num);
            bucketMax[idx] = max(bucketMax[idx], num);
            bucketUsed[idx] = true;
        }

        // Compute max gap
        int maxGap = 0;
        int prevMax = minVal;

        for (int i = 0; i < bucketCount; ++i) {
            if (!bucketUsed[i]) continue;
            maxGap = max(maxGap, bucketMin[i] - prevMax);
            prevMax = bucketMax[i];
        }

        return maxGap;
    }
};
