import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * @lc app=leetcode id=6 lang=java
 *
 * [6] ZigZag Conversion
 *
 * https://leetcode.com/problems/zigzag-conversion/description/
 *
 * algorithms
 * Medium (38.77%)
 * Likes:    2518
 * Dislikes: 6118
 * Total Accepted:    592.4K
 * Total Submissions: 1.5M
 * Testcase Example:  '"PAYPALISHIRING"\n3'
 *
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
 * of rows like this: (you may want to display this pattern in a fixed font for
 * better legibility)
 * 
 * 
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * 
 * 
 * And then read line by line: "PAHNAPLSIIGYIR"
 * 
 * Write the code that will take a string and make this conversion given a
 * number of rows:
 * 
 * 
 * string convert(string s, int numRows);
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "PAYPALISHIRING", numRows = 3
 * Output: "PAHNAPLSIIGYIR"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "PAYPALISHIRING", numRows = 4
 * Output: "PINALSIGYAHRPI"
 * Explanation:
 * P     I    N
 * A   L S  I G
 * Y A   H R
 * P     I
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "A", numRows = 1
 * Output: "A"
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 1000
 * s consists of English letters (lower-case and upper-case), ',' and '.'.
 * 1 <= numRows <= 1000
 * 
 * 
 */

// @lc code=start
class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1){
            return s;
        }
        int cycle = numRows + numRows - 2;
        int n = s.length();
        int cycles = n / cycle;
        HashMap<Integer, ArrayList<Character>> map = new HashMap<Integer, ArrayList<Character>>();
        List<String> res = new ArrayList<String>();
        for(int i = 0; i < numRows; i++){
            map.put(i, new ArrayList<Character>());
        }
        for(int j = 0; j < n; j++){
            int inCycle = j / cycle;
            int order = j % cycle;
            if(order < numRows){
                map.get(order).add(s.charAt(j));
            }else{
                int k = 2*numRows-2-order;
                map.get(k).add(s.charAt(j));
            }
        }
        for(int l = 0; l < numRows; l++){
            res.add(map.get(l).stream().map(String::valueOf).collect(Collectors.joining()));
        }
        return String.join("", res);
    }

    public String convert0(String s, int numRows) {
        // T O(n) S O(1)
        int length = s.length();
        if (numRows > length || numRows <= 1) {
            return s;
        }
        
        char[] zigZagChars = new char[length];
        int count = 0;
        int interval = 2 * numRows - 2;
        
        for (int i = 0; i < numRows; i++) {
            int step = interval - 2 * i;
            for (int j = i; j < length; j+= interval) {
                zigZagChars[count] = s.charAt(j);
                count++;
                if (step > 0 && step < interval && j + step < length) {
                    zigZagChars[count] = s.charAt(j + step);
                    count++;
                }
            }
        }
        return new String(zigZagChars);
    }
}
// @lc code=end

