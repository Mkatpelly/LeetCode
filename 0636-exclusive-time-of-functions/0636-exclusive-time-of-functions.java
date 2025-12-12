class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] result = new int[n];
        Stack<int[]> stack = new Stack<>();
        for (String log : logs) {
            String[] parts = log.split(":");
            int id = Integer.parseInt(parts[0]);
            String type = parts[1];
            int timestamp = Integer.parseInt(parts[2]);

            if (type.equals("start")) {
                stack.push(new int[]{id, timestamp});
            } else {
                int[] startLog = stack.pop();
                int duration = timestamp - startLog[1] + 1;
                result[startLog[0]] += duration;

                if (!stack.isEmpty()) {
                    result[stack.peek()[0]] -= duration;
                }
            }
        }

        return result;
    }
}