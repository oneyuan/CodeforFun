/*
 * @lc app=leetcode id=289 lang=java
 *
 * [289] Game of Life
 *
 * https://leetcode.com/problems/game-of-life/description/
 *
 * algorithms
 * Medium (59.65%)
 * Likes:    4925
 * Dislikes: 450
 * Total Accepted:    352.6K
 * Total Submissions: 535.2K
 * Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
 *
 * According to Wikipedia's article: "The Game of Life, also known simply as
 * Life, is a cellular automaton devised by the British mathematician John
 * Horton Conway in 1970."
 * 
 * The board is made up of an m x n grid of cells, where each cell has an
 * initial state: live (represented by a 1) or dead (represented by a 0). Each
 * cell interacts with its eight neighbors (horizontal, vertical, diagonal)
 * using the following four rules (taken from the above Wikipedia
 * article):
 * 
 * 
 * Any live cell with fewer than two live neighbors dies as if caused by
 * under-population.
 * Any live cell with two or three live neighbors lives on to the next
 * generation.
 * Any live cell with more than three live neighbors dies, as if by
 * over-population.
 * Any dead cell with exactly three live neighbors becomes a live cell, as if
 * by reproduction.
 * 
 * 
 * The next state is created by applying the above rules simultaneously to
 * every cell in the current state, where births and deaths occur
 * simultaneously. Given the current state of the m x n grid board, return the
 * next state.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
 * Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: board = [[1,1],[1,0]]
 * Output: [[1,1],[1,1]]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == board.length
 * n == board[i].length
 * 1 <= m, n <= 25
 * board[i][j] is 0 or 1.
 * 
 * 
 * 
 * Follow up:
 * 
 * 
 * Could you solve it in-place? Remember that the board needs to be updated
 * simultaneously: You cannot update some cells first and then use their
 * updated values to update other cells.
 * In this question, we represent the board using a 2D array. In principle, the
 * board is infinite, which would cause problems when the active area
 * encroaches upon the border of the array (i.e., live cells reach the border).
 * How would you address these problems?
 * 
 * 
 */

// @lc code=start
class Solution {
    public void gameOfLife(int[][] board) {
        int[] neighbors = {-1,0,1};
        int m = board.length;
        if(m == 0){
            return;
        }
        int n = board[0].length;
        int[][] copy = new int[m][n];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                copy[i][j] = board[i][j];
            }
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                int liveNeighbors = 0;
                for(int k = 0; k < 3; k++){
                    for(int l = 0; l < 3; l++){
                        if(!(k == 1 && l == 1)){
                            if((i+ neighbors[k] >= 0 && i+neighbors[k] < m) && (j + neighbors[l] >= 0 && j + neighbors[l] < n) && (copy[i+ neighbors[k]][j + neighbors[l]] == 1)){
                            liveNeighbors++;
                            }
                        }
                        
                    }
                }
                if(board[i][j] == 0 && liveNeighbors == 3){
                    board[i][j] = 1;
                }
                if(board[i][j] == 1 && liveNeighbors < 2){
                    board[i][j] = 0;
                }
                if(board[i][j] == 1 && liveNeighbors  > 3){
                    board[i][j] = 0;
                }
            }
        }
    }

    public void gameOfLife0(int[][] board){
        // 1:[1,1] 0:[0,0] -1:[1,0] 2:[0,1]
        int m = board.length;
        if(m == 0){
            return;
        }
        int n = board[0].length;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                int liveNeighbors = 0;
                for(int k = -1; k < 2; k++){
                    for(int l = -1; l < 2; l++){
                        int px = i + k;
                        int py = j + l;
                        if(!(k == 0 && l == 0)){
                            if((px >= 0 && px < m) && (py >= 0 && py < n) &&(board[px][py] == 1 || board[px][py] == -1)){
                                liveNeighbors++;
                            }
                        }
                    }
                }
                if(board[i][j] == 0 && liveNeighbors == 3){
                    board[i][j] = 2;
                }
                if(board[i][j] == 1 && !(liveNeighbors == 2 || liveNeighbors == 3) ){
                    board[i][j] = -1;
                }
            }
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == -1){
                    board[i][j] = 0;
                }
                if(board[i][j] == 2){
                    board[i][j] = 1;
                }
            }
        }
    }
}
// @lc code=end

