import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

/*
 * @lc app=leetcode id=227 lang=java
 *
 * [227] Basic Calculator II
 *
 * https://leetcode.com/problems/basic-calculator-ii/description/
 *
 * algorithms
 * Medium (39.13%)
 * Likes:    4733
 * Dislikes: 605
 * Total Accepted:    460.2K
 * Total Submissions: 1.1M
 * Testcase Example:  '"3+2*2"'
 *
 * Given a string s which represents an expression, evaluate this expression
 * and return its value. 
 * 
 * The integer division should truncate toward zero.
 * 
 * You may assume that the given expression is always valid. All intermediate
 * results will be in the range of [-2^31, 2^31 - 1].
 * 
 * Note: You are not allowed to use any built-in function which evaluates
 * strings as mathematical expressions, such as eval().
 * 
 * 
 * Example 1:
 * Input: s = "3+2*2"
 * Output: 7
 * Example 2:
 * Input: s = " 3/2 "
 * Output: 1
 * Example 3:
 * Input: s = " 3+5 / 2 "
 * Output: 5
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 3 * 10^5
 * s consists of integers and operators ('+', '-', '*', '/') separated by some
 * number of spaces.
 * s represents a valid expression.
 * All the integers in the expression are non-negative integers in the range
 * [0, 2^31 - 1].
 * The answer is guaranteed to fit in a 32-bit integer.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int calculate(String s) {
        if(s == null || s.isEmpty()){
            return 0;
        }
        Deque<Integer> stack = new ArrayDeque<Integer>();
        int length = s.length();
        int cur = 0;
        int res = 0;
        char operation = '+';
        for(int i = 0; i < length; i++){
            if(Character.isDigit(s.charAt(i))){
                cur = 10*cur + (s.charAt(i) - '0');
            }
            if(!Character.isDigit(s.charAt(i)) && !Character.isWhitespace(s.charAt(i)) || i == length - 1){
                if(operation == '+'){
                    stack.push(cur);
                }else if(operation == '-'){
                    stack.push(-cur);
                }else if(operation == '*'){
                    stack.push(stack.pop()*cur);
                }else if(operation == '/'){
                    stack.push(stack.pop()/cur);
                }
                cur = 0;
                operation = s.charAt(i);
            }
        }
        while(!stack.isEmpty()){
            res += stack.pop();
        }
        return res;
    }

    public int calculate0(String s) {
        if(s == null || s.isEmpty()){
            return 0;
        }
        int res = 0, cur = 0, lastNum = 0;
        char op = '+';
        int n = s.length();
        final List operation = new ArrayList<Character>(List.of('+', '-', '*', '/'));
        for(int i = 0; i < n; i++){
            char curChar = s.charAt(i);
            if(Character.isDigit(curChar)){
                cur = cur *10 + (curChar - '0');
            }
            if(operation.contains(curChar) || i == n-1){
                if(op ==  '+'){
                    res += lastNum;
                    lastNum = cur;
                }else if(op == '-'){
                    res += lastNum;
                    lastNum = -cur;
                }else if(op == '*'){
                    lastNum = lastNum * cur;
                }else if(op == '/'){
                    lastNum = lastNum / cur;
                }
                op = curChar;
                cur = 0;
            }
        }
        res += lastNum;
        return res;
    }
}
// @lc code=end

