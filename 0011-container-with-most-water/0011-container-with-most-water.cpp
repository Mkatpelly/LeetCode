class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxWater = 0;

        while (left < right) {
            // Calculate area: width * min(height[left], height[right])
            int width = right - left;
            int currentArea = width * min(height[left], height[right]);
            maxWater = max(maxWater, currentArea);

            // Move the pointer with the shorter height
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxWater;
    }
};