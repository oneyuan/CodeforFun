/*
 * @lc app=leetcode id=66 lang=java
 *
 * [66] Plus One
 *
 * https://leetcode.com/problems/plus-one/description/
 *
 * algorithms
 * Easy (42.30%)
 * Likes:    2292
 * Dislikes: 3165
 * Total Accepted:    821.3K
 * Total Submissions: 1.9M
 * Testcase Example:  '[1,2,3]'
 *
 * Given a non-empty array of decimal digits representing a non-negative
 * integer, increment one to the integer.
 * 
 * The digits are stored such that the most significant digit is at the head of
 * the list, and each element in the array contains a single digit.
 * 
 * You may assume the integer does not contain any leading zero, except the
 * number 0 itself.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: digits = [1,2,3]
 * Output: [1,2,4]
 * Explanation: The array represents the integer 123.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: digits = [4,3,2,1]
 * Output: [4,3,2,2]
 * Explanation: The array represents the integer 4321.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: digits = [0]
 * Output: [1]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= digits.length <= 100
 * 0 <= digits[i] <= 9
 * 
 * 
 */

// @lc code=start
class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        int [] res = digits.clone();
        for(int i = n-1; i >= 0; i--){
            if(digits[i] < 9){
                res[i] += 1;
                return res;
            }
            res[i] = 0;
        }
        res = new int[n+1];
        res[0] = 1;
        return res;
    }
}
// @lc code=end

