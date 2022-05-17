/*
 * @lc app=leetcode id=283 lang=java
 *
 * [283] Move Zeroes
 *
 * https://leetcode.com/problems/move-zeroes/description/
 *
 * algorithms
 * Easy (58.89%)
 * Likes:    9159
 * Dislikes: 244
 * Total Accepted:    1.7M
 * Total Submissions: 2.7M
 * Testcase Example:  '[0,1,0,3,12]'
 *
 * Given an integer array nums, move all 0's to the end of it while maintaining
 * the relative order of the non-zero elements.
 * 
 * Note that you must do this in-place without making a copy of the array.
 * 
 * 
 * Example 1:
 * Input: nums = [0,1,0,3,12]
 * Output: [1,3,12,0,0]
 * Example 2:
 * Input: nums = [0]
 * Output: [0]
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^4
 * -2^31 <= nums[i] <= 2^31 - 1
 * 
 * 
 * 
 * Follow up: Could you minimize the total number of operations done?
 */

// @lc code=start
class Solution {
    public void moveZeroes(int[] nums) {
        int length = nums.length;
        int lastNonZeroPlace = 0;
        for(int i = 0; i < length; i++){
            if(nums[i] != 0){
                nums[lastNonZeroPlace] = nums[i];
                lastNonZeroPlace++;
            }
        }
        for(int i = lastNonZeroPlace; i < length; i++){
            nums[i] = 0;
        }
    }

    public void moveZeroes0(int[] nums){
        int j = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                int tmp = nums[j];
                nums[j] = nums[i];
                nums[i] = tmp;
                j++;
            }
        }
    }
}
// @lc code=end

