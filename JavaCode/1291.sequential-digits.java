/*
 * @lc app=leetcode id=1291 lang=java
 *
 * [1291] Sequential Digits
 *
 * https://leetcode.com/problems/sequential-digits/description/
 *
 * algorithms
 * Medium (61.33%)
 * Likes:    2533
 * Dislikes: 154
 * Total Accepted:    157.6K
 * Total Submissions: 245.3K
 * Testcase Example:  '100\n300'
 *
 * An integer has sequential digits if and only if each digit in the number is
 * one more than the previous digit.
 * 
 * Return a sorted list of all the integers in the range [low, high] inclusive
 * that have sequential digits.
 * 
 * 
 * Example 1:
 * Input: low = 100, high = 300
 * Output: [123,234]
 * Example 2:
 * Input: low = 1000, high = 13000
 * Output: [1234,2345,3456,4567,5678,6789,12345]
 * 
 * 
 * Constraints:
 * 
 * 
 * 10 <= low <= high <= 10^9
 * 
 * 
 */

// @lc code=start

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> res = new ArrayList<>();
        for (int i = 1; i < 10; i++) {
            int num = i;
            for (int j = i+1; j < 10; j++) {
                num = num * 10 + j;
                if (num >= low && num <= high) {
                    res.add(num);
                }
            }
        }
        res.sort(null);
        return res;
    }
}
// @lc code=end

