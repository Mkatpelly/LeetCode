// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html

class PeekingIterator implements Iterator<Integer> {
	private Iterator<Integer> iterator;
    private Integer nextElement;

    public PeekingIterator(Iterator<Integer> iterator) {
        this.iterator = iterator;
        // Pre-fetch the first element if available
        nextElement = iterator.hasNext() ? iterator.next() : null;
    }

    // Returns the next element without advancing the iterator
    public Integer peek() {
        return nextElement;
    }

    @Override
    public Integer next() {
        Integer current = nextElement;
        // Update cache with the next item (if any)
        nextElement = iterator.hasNext() ? iterator.next() : null;
        return current;
    }

    @Override
    public boolean hasNext() {
        return nextElement != null;
    }
}