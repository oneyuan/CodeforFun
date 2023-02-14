import java.util.Vector;

/*
 * @lc app=leetcode id=79 lang=java
 *
 * [79] Word Search
 *
 * https://leetcode.com/problems/word-search/description/
 *
 * algorithms
 * Medium (37.70%)
 * Likes:    10705
 * Dislikes: 397
 * Total Accepted:    1.1M
 * Total Submissions: 2.7M
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * Given an m x n grid of characters board and a string word, return true if
 * word exists in the grid.
 * 
 * The word can be constructed from letters of sequentially adjacent cells,
 * where adjacent cells are horizontally or vertically neighboring. The same
 * letter cell may not be used more than once.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "ABCCED"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "SEE"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "ABCB"
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == board.length
 * n = board[i].length
 * 1 <= m, n <= 6
 * 1 <= word.length <= 15
 * board and word consists of only lowercase and uppercase English letters.
 * 
 * 
 * 
 * Follow up: Could you use search pruning to make your solution faster with a
 * larger board?
 * 
 */

// @lc code=start
class Solution {
    public boolean exist(char[][] board, String word) {
        int x = board.length;
        if(x == 0){
            return false;
        }
        int y = board[0].length;
        boolean[][] visited = new boolean[x][y];
        for(int i = 0; i < x; i++){
            for(int j = 0; j < y; j++){
                if(checkChar(board, visited, i, j, word, 0)){
                    return true;
                }
            }
        }
        return false;
    }

    public boolean checkChar(char[][] board, boolean[][] visited, int i, int j, String word, int k){
        if(board[i][j] != word.charAt(k)){
            return false;
        }else if(k == word.length() - 1){
            return true;
        }
        visited[i][j] = true;
        int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}};
        boolean res = false;
        for(int[] dir : directions){
            int l = i + dir[0];
            int m = j + dir[1];
            if(l >= 0 && m >= 0 && l < board.length && m < board[0].length){
                if(Boolean.TRUE.equals(!visited[l][m]) && checkChar(board, visited, l, m, word, k+1)){
                    res = true;
                    break;
                }
            }
        }
        visited[i][j] = false;
        return res;
    }
}
// @lc code=end

