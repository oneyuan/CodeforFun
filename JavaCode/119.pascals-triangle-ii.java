/*
 * @lc app=leetcode id=119 lang=java
 *
 * [119] Pascal's Triangle II
 *
 * https://leetcode.com/problems/pascals-triangle-ii/description/
 *
 * algorithms
 * Easy (52.87%)
 * Likes:    1380
 * Dislikes: 225
 * Total Accepted:    376.8K
 * Total Submissions: 711.5K
 * Testcase Example:  '3'
 *
 * Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the
 * Pascal's triangle.
 * 
 * In Pascal's triangle, each number is the sum of the two numbers directly
 * above it as shown:
 * 
 * 
 * Example 1:
 * Input: rowIndex = 3
 * Output: [1,3,3,1]
 * Example 2:
 * Input: rowIndex = 0
 * Output: [1]
 * Example 3:
 * Input: rowIndex = 1
 * Output: [1,1]
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= rowIndex <= 33
 * 
 * 
 * 
 * Follow up: Could you optimize your algorithm to use only O(rowIndex) extra
 * space?
 * 
 */

// @lc code=start
class Solution {
    public List<Integer> getRow(int rowIndex) {
        Integer numRows = rowIndex+1;
        List<Integer> tmp = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        tmp.add(1);
        res.add(tmp);
        if(numRows == 1){
            return tmp;
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
        return res.get(rowIndex);
    }
}
// @lc code=end

