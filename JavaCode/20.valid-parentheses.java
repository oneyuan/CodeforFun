import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Stack;

/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (39.92%)
 * Likes:    7071
 * Dislikes: 294
 * Total Accepted:    1.4M
 * Total Submissions: 3.4M
 * Testcase Example:  '"()"'
 *
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * 
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "()"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "()[]{}"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "(]"
 * Output: false
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: s = "([)]"
 * Output: false
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: s = "{[]}"
 * Output: true
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^4
 * s consists of parentheses only '()[]{}'.
 * 
 * 
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<>();
        HashMap leftToRight = new HashMap<Character,Character>(3){{
            put('(',')');
            put('[',']');
            put('{','}');
        }};
        Integer n = s.length();
        for(int i=0; i < n; i++){
            Character tmp = s.charAt(i);
            if(leftToRight.containsKey(tmp)){
                brackets.push(tmp);
            }else{
                if(brackets.isEmpty()){
                    brackets.push('#');
                }
                Character left = brackets.pop();
                if(tmp != leftToRight.get(left)){
                    return false;
                }
            }
        }
        if(brackets.isEmpty()){
            return true;
        }else{
            return false;
        }
    }
}
// @lc code=end

