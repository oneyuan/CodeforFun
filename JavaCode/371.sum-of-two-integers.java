/*
 * @lc app=leetcode id=371 lang=java
 *
 * [371] Sum of Two Integers
 *
 * https://leetcode.com/problems/sum-of-two-integers/description/
 *
 * algorithms
 * Medium (50.60%)
 * Likes:    2163
 * Dislikes: 3313
 * Total Accepted:    265.1K
 * Total Submissions: 523.5K
 * Testcase Example:  '1\n2'
 *
 * Given two integers a and b, return the sum of the two integers without using
 * the operators + and -.
 * 
 * 
 * Example 1:
 * Input: a = 1, b = 2
 * Output: 3
 * Example 2:
 * Input: a = 2, b = 3
 * Output: 5
 * 
 * 
 * Constraints:
 * 
 * 
 * -1000 <= a, b <= 1000
 * 
 * 
 */

// @lc code=start
class Solution {
    public int getSum(int a, int b) {
        if (b == 0) return a;
        int sum;
        int carry;
        sum = a ^ b;
        carry = (a & b) << 1;
        return getSum(sum, carry);
    }
}
// @lc code=end

