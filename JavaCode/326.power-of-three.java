/*
 * @lc app=leetcode id=326 lang=java
 *
 * [326] Power of Three
 *
 * https://leetcode.com/problems/power-of-three/description/
 *
 * algorithms
 * Easy (42.49%)
 * Likes:    915
 * Dislikes: 118
 * Total Accepted:    456.1K
 * Total Submissions: 1M
 * Testcase Example:  '27'
 *
 * Given an integer n, return true if it is a power of three. Otherwise, return
 * false.
 * 
 * An integer n is a power of three, if there exists an integer x such that n
 * == 3^x.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 27
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 0
 * Output: false
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: n = 9
 * Output: true
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * -2^31 <= n <= 2^31 - 1
 * 
 * 
 * 
 * Follow up: Could you solve it without loops/recursion?
 */

// @lc code=start
class Solution {
    public boolean isPowerOfThree(int n) {
        return (Math.log10(n)/Math.log10(3)) % 1 == 0;
    }
}
// @lc code=end

