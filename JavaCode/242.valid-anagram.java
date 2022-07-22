/*
 * @lc app=leetcode id=242 lang=java
 *
 * [242] Valid Anagram
 *
 * https://leetcode.com/problems/valid-anagram/description/
 *
 * algorithms
 * Easy (59.30%)
 * Likes:    5671
 * Dislikes: 231
 * Total Accepted:    1.4M
 * Total Submissions: 2.3M
 * Testcase Example:  '"anagram"\n"nagaram"'
 *
 * Given two strings s and t, return true if t is an anagram of s, and false
 * otherwise.
 * 
 * An Anagram is a word or phrase formed by rearranging the letters of a
 * different word or phrase, typically using all the original letters exactly
 * once.
 * 
 * 
 * Example 1:
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 * Example 2:
 * Input: s = "rat", t = "car"
 * Output: false
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length, t.length <= 5 * 10^4
 * s and t consist of lowercase English letters.
 * 
 * 
 * 
 * Follow up: What if the inputs contain Unicode characters? How would you
 * adapt your solution to such a case?
 * 
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        int[] sCount = new int[26];
        int[] tCount = new int[26];
        for(char i : s.toCharArray()){
            sCount[i-'a'] += 1; 
        }
        for(char j : t.toCharArray()){
            tCount[j-'a'] += 1;
        }
        for(int k = 0; k < 26; k++){
            if(sCount[k] != tCount[k]){
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

