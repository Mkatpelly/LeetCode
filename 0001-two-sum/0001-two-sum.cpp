class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap; // Key: number, Value: index

        for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];

        // Check if complement is already in the hash map
        if (numMap.find(complement) != numMap.end()) {
            return {numMap[complement], i}; // Found the pair
        }

        // Store the current number and its index
        numMap[nums[i]] = i;
    }

    return {}; // This will never be reached as per problem constraints        
    }
};