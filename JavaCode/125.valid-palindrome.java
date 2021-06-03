/*
 * @lc app=leetcode id=125 lang=java
 *
 * [125] Valid Palindrome
 *
 * https://leetcode.com/problems/valid-palindrome/description/
 *
 * algorithms
 * Easy (30.97%)
 * Likes:    582
 * Dislikes: 1707
 * Total Accepted:    354.8K
 * Total Submissions: 1.1M
 * Testcase Example:  '"A man, a plan, a canal: Panama"'
 *
 * Given a string, determine if it is a palindrome, considering only
 * alphanumeric characters and ignoring cases.
 * 
 * Note: For the purpose of this problem, we define empty string as valid
 * palindrome.
 * 
 * Example 1:
 * 
 * 
 * Input: "A man, a plan, a canal: Panama"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "race a car"
 * Output: false
 * 
 * 
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder reverse = new StringBuilder();
        int n = s.length();
        for(int i=0; i < n; i++){
            if(Character.isLetterOrDigit(s.charAt(i))){
                reverse.append(s.charAt(i));
            }
        }
        String inOrder = new String(reverse);
        String r = new String(reverse.reverse());
        if(r.equalsIgnoreCase(inOrder)){
            return true;
        }
        return false;
    }
}
// @lc code=end

