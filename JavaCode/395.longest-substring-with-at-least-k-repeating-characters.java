import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode id=395 lang=java
 *
 * [395] Longest Substring with At Least K Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
 *
 * algorithms
 * Medium (43.84%)
 * Likes:    3424
 * Dislikes: 303
 * Total Accepted:    142.9K
 * Total Submissions: 322.5K
 * Testcase Example:  '"aaabb"\n3'
 *
 * Given a string s and an integer k, return the length of the longest
 * substring of s such that the frequency of each character in this substring
 * is greater than or equal to k.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "aaabb", k = 3
 * Output: 3
 * Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "ababbc", k = 2
 * Output: 5
 * Explanation: The longest substring is "ababb", as 'a' is repeated 2 times
 * and 'b' is repeated 3 times.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^4
 * s consists of only lowercase English letters.
 * 1 <= k <= 10^5
 * 
 * 
 */

// @lc code=start
class Solution {
    public int longestSubstring(String s, int k) {
        int res = 0;
        Map<Character, Integer> count = new HashMap<>(26);
        Map<Character, Integer> subString = new HashMap<>(26);
        for(int i = 0; i < s.length(); i++){
            count.put(s.charAt(i), count.getOrDefault(s.charAt(i), 0)+1);
        }
        int maxUnique = count.size();
        for(int cur = 1; cur <= maxUnique; cur++){
            int startIndex = 0;
            int endIndex = 0;
            int unique = 0;
            int uniqueThanK = 0;
            subString.clear();
            while(endIndex < s.length()){
                char startChar = s.charAt(startIndex);
                char endChar = s.charAt(endIndex);
                if(unique <= cur){
                    if(!subString.containsKey(endChar) || subString.get(endChar) == 0){
                        unique++;
                    }
                    subString.put(endChar, subString.getOrDefault(endChar, 0)+1);
                    if(subString.get(endChar) == k){
                        uniqueThanK++;
                    }
                    endIndex++;
                }else{
                    if(subString.get(startChar) == k){
                        uniqueThanK--;
                    }
                    subString.put(startChar, subString.get(startChar)-1);
                    if(subString.get(startChar) == 0){
                        unique--;
                    }
                    startIndex++;
                }
                if(unique == cur && unique == uniqueThanK){
                    System.out.println(startIndex+" "+endIndex+" "+ res);
                    res = Math.max(endIndex - startIndex, res);
                }
            }
        }
        return res;
    }

    public int longestSubstring1(String s, int k) {
        if (s == null || s.length() == 0 || s.length() < k)
            return 0;
        
        int[] count = new int[26];
        char[] chs = s.toCharArray();
        boolean entireStringIsValid = true;
        
        for (Character c : chs) {
            count[c - 'a']++;
        }
        
        for (Character c : chs) {
            if (count[c - 'a'] > 0 && count[c - 'a'] < k) {
                entireStringIsValid = false;
                break;
            }
        }
        
        if (entireStringIsValid)
            return s.length();
        
        //找出导致entireStringIsValid是false的点，在前后进行recursive call
        //只有在找到这样的点的时候更新left，shrink当前substring去寻找下一段
        int left = 0, right = 0;
        int ans = Integer.MIN_VALUE;
        while (right < chs.length) {
            Character c = chs[right];
            if (count[c - 'a'] < k) {
                ans = Math.max(ans, longestSubstring(s.substring(left, right), k));
                left = right + 1;
            }
            right++;
        }
        
        //这里要更新一下ans,很容易忘记，因为right虽然越界了，但是left到最后有可能会有longer的答案
        ans = Math.max(ans, longestSubstring(s.substring(left), k));
        return ans;
    }
}
// @lc code=end

