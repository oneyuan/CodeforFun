/*
 * @lc app=leetcode id=67 lang=java
 *
 * [67] Add Binary
 *
 * https://leetcode.com/problems/add-binary/description/
 *
 * algorithms
 * Easy (47.09%)
 * Likes:    2714
 * Dislikes: 341
 * Total Accepted:    593.9K
 * Total Submissions: 1.3M
 * Testcase Example:  '"11"\n"1"'
 *
 * Given two binary strings a and b, return their sum as a binary string.
 * 
 * 
 * Example 1:
 * Input: a = "11", b = "1"
 * Output: "100"
 * Example 2:
 * Input: a = "1010", b = "1011"
 * Output: "10101"
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= a.length, b.length <= 10^4
 * a and b consist only of '0' or '1' characters.
 * Each string does not contain leading zeros except for the zero itself.
 * 
 * 
 */

// @lc code=start
class Solution {
    public String addBinary(String a, String b) {
        int an = a.length();
        int bn = b.length();
        StringBuilder sb = new StringBuilder();
        int i = an-1;
        int j = bn-1;
        int carry = 0;
        while(i >= 0 || j >= 0){
            int sum = carry;
            if(i >= 0){
                sum += (a.charAt(i--)-'0');
            }
            if(j >= 0){
                sum += (b.charAt(j--)-'0');
            }
            sb.append(sum%2);
            carry = sum/2;
        }
        if(carry!=0){
            sb.append(carry);
        }
        return sb.reverse().toString();
    }
}
// @lc code=end

