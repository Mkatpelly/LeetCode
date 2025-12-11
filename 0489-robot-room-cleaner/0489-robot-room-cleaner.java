/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * interface Robot {
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     public boolean move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     public void turnLeft();
 *     public void turnRight();
 *
 *     // Clean the current cell.
 *     public void clean();
 * }
 */

class Solution {
    private static final int[][] DIRECTIONS = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    private Set<String> visited = new HashSet<>();
    private Robot robot;
    public void cleanRoom(Robot robot) {
        this.robot = robot;
        dfs(0, 0, 0);
    }
    private void dfs(int row, int col, int direction) {
        String position = row + "," + col;
        if (visited.contains(position)) {
            return;
        }
        robot.clean();
        visited.add(position);
        for (int i = 0; i < 4; i++) {
            if (robot.move()) {
                int newRow = row + DIRECTIONS[direction][0];
                int newCol = col + DIRECTIONS[direction][1];
                dfs(newRow, newCol, direction);
                robot.turnLeft();
                robot.turnLeft();
                robot.move();
                robot.turnLeft();
                robot.turnLeft();
            }
            robot.turnRight();
            direction = (direction + 1) % 4;
        }
    }
}