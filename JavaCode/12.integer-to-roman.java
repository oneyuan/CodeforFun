import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

/*
 * @lc app=leetcode id=12 lang=java
 *
 * [12] Integer to Roman
 *
 * https://leetcode.com/problems/integer-to-roman/description/
 *
 * algorithms
 * Medium (57.53%)
 * Likes:    1918
 * Dislikes: 3281
 * Total Accepted:    512.4K
 * Total Submissions: 889K
 * Testcase Example:  '3'
 *
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D
 * and M.
 * 
 * 
 * Symbol       Value
 * I             1
 * V             5
 * X             10
 * L             50
 * C             100
 * D             500
 * M             1000
 * 
 * For example, 2 is written as II in Roman numeral, just two one's added
 * together. 12 is written as XII, which is simply X + II. The number 27 is
 * written as XXVII, which is XX + V + II.
 * 
 * Roman numerals are usually written largest to smallest from left to right.
 * However, the numeral for four is not IIII. Instead, the number four is
 * written as IV. Because the one is before the five we subtract it making
 * four. The same principle applies to the number nine, which is written as IX.
 * There are six instances where subtraction is used:
 * 
 * 
 * I can be placed before V (5) and X (10) to make 4 and 9. 
 * X can be placed before L (50) and C (100) to make 40 and 90. 
 * C can be placed before D (500) and M (1000) to make 400 and 900.
 * 
 * 
 * Given an integer, convert it to a roman numeral.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: num = 3
 * Output: "III"
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: num = 4
 * Output: "IV"
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: num = 9
 * Output: "IX"
 * 
 * 
 * Example 4:
 * 
 * 
 * Input: num = 58
 * Output: "LVIII"
 * Explanation: L = 50, V = 5, III = 3.
 * 
 * 
 * Example 5:
 * 
 * 
 * Input: num = 1994
 * Output: "MCMXCIV"
 * Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= num <= 3999
 * 
 * 
 */

// @lc code=start
class Solution {
    public String intToRoman(int num) {
        HashMap map = new HashMap<Integer, String>();
        map.put(1, "I");
        map.put(4, "IV");
        map.put(5, "V");
        map.put(9, "IX");
        map.put(10, "X");
        map.put(40, "XL");
        map.put(50, "L");
        map.put(90, "XC");
        map.put(100, "C");
        map.put(400, "CD");
        map.put(500, "D");
        map.put(900, "CM");
        map.put(1000, "M");
        StringBuilder res = new StringBuilder();
        List<Integer> divide = new ArrayList<>();
        divide.addAll(map.keySet());
        divide.sort(Comparator.naturalOrder());
        for(int n = 12; n >= 0; n--){
            int d = divide.get(n);
            int time = num / d;
            num = num % d;
            res.append(map.get(d).toString().repeat(time));
        }
        return res.toString();
    }

    public String intToRoman(int num){
        if (num <= 0 || num > 3999) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        int i = 0;
        while (num > 0) {
            while (num >= values[i]) {
                num -= values[i];
                sb.append(roman[i]);
            }
            i++;
        }
        return sb.toString();
    }
}
// @lc code=end

