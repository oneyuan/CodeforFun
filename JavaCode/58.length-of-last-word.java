/*
 * @lc app=leetcode id=58 lang=java
 *
 * [58] Length of Last Word
 *
 * https://leetcode.com/problems/length-of-last-word/description/
 *
 * algorithms
 * Easy (33.49%)
 * Likes:    1061
 * Dislikes: 3142
 * Total Accepted:    495.8K
 * Total Submissions: 1.5M
 * Testcase Example:  '"Hello World"'
 *
 * Given a string s consists of some words separated by spaces, return the
 * length of the last word in the string. If the last word does not exist,
 * return 0.
 * 
 * A word is a maximal substring consisting of non-space characters only.
 * 
 * 
 * Example 1:
 * Input: s = "Hello World"
 * Output: 5
 * Example 2:
 * Input: s = " "
 * Output: 0
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^4
 * s consists of only English letters and spaces ' '.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        String[] c = s.split(" ");
        if(c.length < 1){
            return 0;
        }
        return c[c.length-1].length();
    }
}
// @lc code=end

