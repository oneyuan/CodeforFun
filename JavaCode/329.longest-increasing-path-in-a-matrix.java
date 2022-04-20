import java.util.ArrayList;

/*
 * @lc app=leetcode id=329 lang=java
 *
 * [329] Longest Increasing Path in a Matrix
 *
 * https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
 *
 * algorithms
 * Hard (46.94%)
 * Likes:    5182
 * Dislikes: 87
 * Total Accepted:    318.4K
 * Total Submissions: 641.5K
 * Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
 *
 * Given an m x n integers matrix, return the length of the longest increasing
 * path in matrix.
 * 
 * From each cell, you can either move in four directions: left, right, up, or
 * down. You may not move diagonally or move outside the boundary (i.e.,
 * wrap-around is not allowed).
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
 * Output: 4
 * Explanation: The longest increasing path is [1, 2, 6, 9].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
 * Output: 4
 * Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
 * is not allowed.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: matrix = [[1]]
 * Output: 1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 200
 * 0 <= matrix[i][j] <= 2^31 - 1
 * 
 * 
 */

// @lc code=start
class Solution {

    public final static int[][] steeringWell = {{-1, 0},{1, 0},{0, -1},{0, 1}};

    public int longestIncreasingPath(int[][] matrix) {
        if(matrix.length == 0){
            return 0;
        }
        int res = 1;
        int m = matrix.length;
        int n = matrix[0].length;
        int [][] cache = new int[m][n];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                int tmp = dfs(matrix, m, n, i, j, cache);
                res = Math.max(res, tmp);
            }
        }
        return res;
    }

    public int dfs(int[][] matrix, int m, int n, int i, int j, int[][] cache){
        if(cache[i][j] != 0){
            return cache[i][j];
        }
        int max = 1;
        for(int[] t : steeringWell){
            int x = i + t[0];
            int y = j + t[1];
            if(x < 0 || y < 0 || x >= m || y >= n || matrix[x][y] <= matrix[i][j]){
                continue;
            }
            int path = 1 + dfs(matrix, m, n, x, y, cache);
            max = Math.max(max, path);
        }
        cache[i][j] = max;
        return cache[i][j];
    }
}
// @lc code=end

