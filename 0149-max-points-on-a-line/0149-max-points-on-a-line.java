class Solution {
    public int maxPoints(int[][] points) {
        if (points.length < 3) return points.length;
        int maxCount = 1;
        for (int i = 0; i < points.length; i++) {
            Map<String, Integer> slopeMap = new HashMap<>();
            int duplicates = 0, verticals = 0, localMax = 1;
            
            for (int j = i + 1; j < points.length; j++) {
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                if (dx == 0 && dy == 0) {
                    duplicates++;
                    continue;
                }
                
                if (dx == 0) {
                    verticals++;
                    localMax = Math.max(localMax, verticals + 1);
                    continue;
                }
                int gcd = gcd(dx, dy);
                dx /= gcd;
                dy /= gcd;
                String slope = dy + "/" + dx;
                slopeMap.put(slope, slopeMap.getOrDefault(slope, 1) + 1);
                localMax = Math.max(localMax, slopeMap.get(slope));
            }
            
            maxCount = Math.max(maxCount, localMax + duplicates);
        }
        return maxCount;
    }
    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}