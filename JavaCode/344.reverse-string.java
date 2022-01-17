/*
 * @lc app=leetcode id=344 lang=java
 *
 * [344] Reverse String
 *
 * https://leetcode.com/problems/reverse-string/description/
 *
 * algorithms
 * Easy (71.25%)
 * Likes:    3711
 * Dislikes: 879
 * Total Accepted:    1.4M
 * Total Submissions: 1.8M
 * Testcase Example:  '["h","e","l","l","o"]'
 *
 * Write a function that reverses a string. The input string is given as an
 * array of characters s.
 * 
 * You must do this by modifying the input array in-place with O(1) extra
 * memory.
 * 
 * 
 * Example 1:
 * Input: s = ["h","e","l","l","o"]
 * Output: ["o","l","l","e","h"]
 * Example 2:
 * Input: s = ["H","a","n","n","a","h"]
 * Output: ["h","a","n","n","a","H"]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s[i] is a printable ascii character.
 * 
 * 
 */

// @lc code=start
class Solution {
    public void reverseString(char[] s) {
        int length = s.length;
        int left = 0;
        int right = length-1;
        while(left < right){
            swap(s, left, right);
            left++;
            right--;
        }
    }

    public void swap(char[] s, int left, int right){
        char tmp = s[left];
        s[left] = s[right];
        s[right] = tmp;
    }
}
// @lc code=end

