class RandomizedCollection {
    private List<Integer> nums;
    private Map<Integer, Set<Integer>> idx;
    private Random rand;

    public RandomizedCollection() {
        nums = new ArrayList<>();
        idx = new HashMap<>();
        rand = new Random();
    }

    public boolean insert(int val) {
        boolean notPresent = !idx.containsKey(val) || idx.get(val).isEmpty();
        idx.putIfAbsent(val, new HashSet<>());
        idx.get(val).add(nums.size());
        nums.add(val);
        return notPresent;
    }

    public boolean remove(int val) {
        if (!idx.containsKey(val) || idx.get(val).isEmpty())
            return false;
        // Get an arbitrary index of val and remove it
        int removeIdx = idx.get(val).iterator().next();
        idx.get(val).remove(removeIdx);

        int lastNum = nums.get(nums.size() - 1);
        nums.set(removeIdx, lastNum); // move lastNum to removeIdx
        // Update the index mapping for lastNum
        if (idx.containsKey(lastNum)) {
            idx.get(lastNum).add(removeIdx);
            idx.get(lastNum).remove(nums.size() - 1);
        }
        nums.remove(nums.size() - 1);
        return true;
    }

    public int getRandom() {
        int randIdx = rand.nextInt(nums.size());
        return nums.get(randIdx);
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */