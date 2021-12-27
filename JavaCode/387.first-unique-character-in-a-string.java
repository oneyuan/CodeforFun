import java.util.Arrays;

/*
 * @lc app=leetcode id=387 lang=java
 *
 * [387] First Unique Character in a String
 *
 * https://leetcode.com/problems/first-unique-character-in-a-string/description/
 *
 * algorithms
 * Easy (54.46%)
 * Likes:    4144
 * Dislikes: 176
 * Total Accepted:    915.1K
 * Total Submissions: 1.6M
 * Testcase Example:  '"leetcode"'
 *
 * Given a string s, find the first non-repeating character in it and return
 * its index. If it does not exist, return -1.
 * 
 * 
 * Example 1:
 * Input: s = "leetcode"
 * Output: 0
 * Example 2:
 * Input: s = "loveleetcode"
 * Output: 2
 * Example 3:
 * Input: s = "aabb"
 * Output: -1
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s consists of only lowercase English letters.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        int[] index = new int[26];
        int res = -1;
        Arrays.fill(index, -1);
        for(int i = 0; i < s.length(); i++){
            int idx = s.charAt(i) - 'a';
            count[idx]++;
        }
        for(int j = 0; j < s.length(); j++){
            if(count[s.charAt(j)-'a'] == 1){
                res = j;
                break;
            }
        }
        return res;
    }

    public int firstUniqChar1(String s) {
        int resIndex = s.length();
        
        if(resIndex == 0) return -1;
        
        for(char c = 'a';c<='z';c++){ 
            int index = s.indexOf(c);
            if(index!=-1 && index == s.lastIndexOf(c))
                resIndex = Math.min(resIndex,index);
        }
        
        return resIndex == s.length() ? -1 : resIndex;
    }
}
// @lc code=end

