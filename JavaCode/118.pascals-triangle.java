/*
 * @lc app=leetcode id=118 lang=java
 *
 * [118] Pascal's Triangle
 *
 * https://leetcode.com/problems/pascals-triangle/description/
 *
 * algorithms
 * Easy (56.11%)
 * Likes:    2595
 * Dislikes: 136
 * Total Accepted:    498.7K
 * Total Submissions: 886.1K
 * Testcase Example:  '5'
 *
 * Given an integer numRows, return the first numRows of Pascal's triangle.
 * 
 * In Pascal's triangle, each number is the sum of the two numbers directly
 * above it as shown:
 * 
 * 
 * Example 1:
 * Input: numRows = 5
 * Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
 * Example 2:
 * Input: numRows = 1
 * Output: [[1]]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= numRows <= 30
 * 
 * 
 */

// @lc code=start
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<Integer> tmp = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        tmp.add(1);
        res.add(tmp);
        if(numRows == 1){
            return res;
        }
        for(int i = 1; i< numRows; i++){
            List<Integer> lastRow = res.get(i-1);
            Integer size = lastRow.size();
            List<Integer> row = new ArrayList<>();
            row.add(1);
            for(int j = 1; j < size; j++){
                row.add(lastRow.get(j-1) + lastRow.get(j));
            }
            row.add(1);
            res.add(row);
        }
        return res;
    }
}
// @lc code=end

