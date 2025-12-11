class Solution {
    public boolean verifyPreorder(int[] preorder) {
        Stack<Integer> stack = new Stack<>();
        int lower = Integer.MIN_VALUE;
        for (int value : preorder) {
            if (value < lower) {
                return false;
            }
            while (!stack.isEmpty() && value > stack.peek()) {
                lower = stack.pop(); 
            }
            stack.push(value);
        }
        
        return true;
    }
}