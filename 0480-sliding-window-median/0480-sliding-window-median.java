class Solution {
    
    private static TreeMap<Integer, Integer> maxHeap;
    private static TreeMap<Integer, Integer> minHeap;
    private static int maxHeapSize;
    private static int minHeapSize;

    public static double[] medianSlidingWindow(int[] nums, int k) {
        maxHeap = new TreeMap<>(Collections.reverseOrder());
        minHeap = new TreeMap<>();
        maxHeapSize = 0;
        minHeapSize = 0;
        int n = nums.length;
        double[] result = new double[n - k + 1];

        for (int i = 0; i < nums.length; i++) {
            add(nums[i]);

            if (i >= k - 1) {
                result[i - k + 1] = findMedian();
                remove(nums[i - k + 1]);
            }
        }

        return result;
    }

    private static void add(int num) {
        if (maxHeapSize == 0 || num <= maxHeap.firstKey()) {
            maxHeap.put(num, maxHeap.getOrDefault(num, 0) + 1);
            maxHeapSize++;
        } else {
            minHeap.put(num, minHeap.getOrDefault(num, 0) + 1);
            minHeapSize++;
        }
        balanceHeaps();
    }

    private static void remove(int num) {
        if (maxHeap.containsKey(num)) {
            if (maxHeap.get(num) == 1) {
                maxHeap.remove(num);
            } else {
                maxHeap.put(num, maxHeap.get(num) - 1);
            }
            maxHeapSize--;
        } else {
            if (minHeap.get(num) == 1) {
                minHeap.remove(num);
            } else {
                minHeap.put(num, minHeap.get(num) - 1);
            }
            minHeapSize--;
        }
        balanceHeaps();
    }

    private static void balanceHeaps() {
        if (maxHeapSize > minHeapSize + 1) {
            move(maxHeap, minHeap);
            maxHeapSize--;
            minHeapSize++;
        } else if (minHeapSize > maxHeapSize) {
            move(minHeap, maxHeap);
            minHeapSize--;
            maxHeapSize++;
        }
    }

    private static void move(TreeMap<Integer, Integer> from, TreeMap<Integer, Integer> to) {
        int num = from.firstKey();
        if (from.get(num) == 1) {
            from.remove(num);
        } else {
            from.put(num, from.get(num) - 1);
        }
        to.put(num, to.getOrDefault(num, 0) + 1);
    }

    private static double findMedian() {
        if (maxHeapSize == minHeapSize) {
            return ((double) maxHeap.firstKey() + minHeap.firstKey()) / 2.0;
        } else {
            return maxHeap.firstKey();
        }
    }
}