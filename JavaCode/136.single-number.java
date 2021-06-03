import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

/*
 * @lc app=leetcode id=136 lang=java
 *
 * [136] Single Number
 *
 * https://leetcode.com/problems/single-number/description/
 *
 * algorithms
 * Easy (66.91%)
 * Likes:    6380
 * Dislikes: 206
 * Total Accepted:    1.2M
 * Total Submissions: 1.8M
 * Testcase Example:  '[2,2,1]'
 *
 * Given a non-empty array of integers nums, every element appears twice except
 * for one. Find that single one.
 * 
 * You must implement a solution with a linear runtime complexity and use only
 * constant extra space.
 * 
 * 
 * Example 1:
 * Input: nums = [2,2,1]
 * Output: 1
 * Example 2:
 * Input: nums = [4,1,2,1,2]
 * Output: 4
 * Example 3:
 * Input: nums = [1]
 * Output: 1
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 3 * 10^4
 * -3 * 10^4 <= nums[i] <= 3 * 10^4
 * Each element in the array appears twice except for one element which appears
 * only once.
 * 
 * 
 */

// @lc code=start
class Solution {
    public int singleNumber(int[] nums) {
        Map<Integer, Integer> h = new HashMap<>();
        for(int i: nums){
            if(!h.containsKey(i)){
                h.put(i, 1);
            }else{
                h.remove(i);
            }
        }
        Iterator<Integer> i = h.keySet().iterator();
        if(i.hasNext()){
            return i.next();
        }else{
            return 0;
        }
    }
}
// @lc code=end

