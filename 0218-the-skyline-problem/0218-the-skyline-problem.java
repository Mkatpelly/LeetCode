class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<int[]> events = new ArrayList<>();
        for (int[] building : buildings) {
            events.add(new int[]{building[0], -building[2]}); // entering: negative height
            events.add(new int[]{building[1], building[2]});  // exiting: positive height
        }
        events.sort((a, b) -> (a[0] != b[0])
                ? a[0] - b[0]
                : a[1] - b[1]);
        
        List<List<Integer>> result = new ArrayList<>();
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        Map<Integer, Integer> countMap = new HashMap<>();
        heap.add(0);
        countMap.put(0, 1);

        int prevMax = 0;
        for (int[] evt : events) {
            int x = evt[0], h = evt[1];
            if (h < 0) {
                heap.add(-h);
                countMap.put(-h, countMap.getOrDefault(-h, 0) + 1);
            } else {
                countMap.put(h, countMap.getOrDefault(h, 0) - 1);
            }
            // Clean up: remove heights with count 0 at the top
            while (!heap.isEmpty() && countMap.getOrDefault(heap.peek(), 0) == 0) heap.poll();
            int curMax = heap.peek();
            if (prevMax != curMax) {
                result.add(List.of(x, curMax));
                prevMax = curMax;
            }
        }
        return result;
    }
}