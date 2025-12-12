class Solution {
    private static final int[][] DIRECTIONS = {
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1},         {0, 1},
        {1, -1}, {1, 0}, {1, 1}
    };
    public char[][] updateBoard(char[][] board, int[] click) {
        int row = click[0];
        int col = click[1];

        if (board[row][col] == 'M') {
            board[row][col] = 'X';
            return board;
        }

        reveal(board, row, col);
        return board;

    }
    private void reveal(char[][] board, int row, int col) {
        int mineCount = countAdjacentMines(board, row, col);

        if (mineCount > 0) {
            board[row][col] = (char) ('0' + mineCount);
        } else {
            board[row][col] = 'B';
            for (int[] direction : DIRECTIONS) {
                int newRow = row + direction[0];
                int newCol = col + direction[1];
                if (isInBounds(board, newRow, newCol) && board[newRow][newCol] == 'E') {
                    reveal(board, newRow, newCol);
                }
            }
        }
    }
     private int countAdjacentMines(char[][] board, int row, int col) {
        int mineCount = 0;
        for (int[] direction : DIRECTIONS) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            if (isInBounds(board, newRow, newCol) && board[newRow][newCol] == 'M') {
                mineCount++;
            }
        }
        return mineCount;
    }

    private boolean isInBounds(char[][] board, int row, int col) {
        return row >= 0 && row < board.length && col >= 0 && col < board[0].length;
    }
}