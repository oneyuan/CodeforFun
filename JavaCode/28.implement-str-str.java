/*
 * @lc app=leetcode id=28 lang=java
 *
 * [28] Implement strStr()
 *
 * https://leetcode.com/problems/implement-strstr/description/
 *
 * algorithms
 * Easy (35.27%)
 * Likes:    2294
 * Dislikes: 2342
 * Total Accepted:    862.5K
 * Total Submissions: 2.4M
 * Testcase Example:  '"hello"\n"ll"'
 *
 * Implement strStr().
 * 
 * Return the index of the first occurrence of needle in haystack, or -1 if
 * needle is not part of haystack.
 * 
 * Clarification:
 * 
 * What should we return when needle is an empty string? This is a great
 * question to ask during an interview.
 * 
 * For the purpose of this problem, we will return 0 when needle is an empty
 * string. This is consistent to C's strstr() and Java's indexOf().
 * 
 * 
 * Example 1:
 * Input: haystack = "hello", needle = "ll"
 * Output: 2
 * Example 2:
 * Input: haystack = "aaaaa", needle = "bba"
 * Output: -1
 * Example 3:
 * Input: haystack = "", needle = ""
 * Output: 0
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= haystack.length, needle.length <= 5 * 10^4
 * haystack and needle consist of only lower-case English characters.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int strStr(String haystack, String needle) {
        for(int i = 0; ; i++){
            for(int j = 0; ; j++){
                if(j == needle.length()){
                    return i;
                }
                if(i + j == haystack.length()){
                    return -1;
                }
                if(haystack.charAt(i+j) != needle.charAt(j)){
                    break;
                }
            }
        }
    }
}
// @lc code=end

