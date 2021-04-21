/*
 * @lc app=leetcode id=53 lang=java
 *
 * [53] Maximum Subarray
 *
 * https://leetcode.com/problems/maximum-subarray/description/
 *
 * algorithms
 * Easy (47.80%)
 * Likes:    11614
 * Dislikes: 559
 * Total Accepted:    1.4M
 * Total Submissions: 2.9M
 * Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
 *
 * Given an integer array nums, find the contiguous subarray (containing at
 * least one number) which has the largest sum and return its sum.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
 * Output: 6
 * Explanation: [4,-1,2,1] has the largest sum = 6.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1]
 * Output: 1
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [5,4,-1,7,8]
 * Output: 23
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 3 * 10^4
 * -10^5 <= nums[i] <= 10^5
 * 
 * 
 * 
 * Follow up: If you have figured out the O(n) solution, try coding another
 * solution using the divide and conquer approach, which is more subtle.
 */

// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int res = Integer.MIN_VALUE;
        int[] matrix = new int[n];
        for(int i = 0; i < n; i++){
            matrix[i] = nums[i];
            if(matrix[i] > res ){
                res = matrix[i];
            }
            for(int j = i+1; j < n; j++){
                matrix[j] = matrix[j-1]+nums[j];
                if(matrix[j] > res ){
                    res = matrix[j];
                }
            }
        }
        return res;
    }

    public int maxSubArray1(int[] nums) {
        int n = nums.length;
        int res = Integer.MIN_VALUE;
        int sum = 0;
        for(int i = 0; i < n; i++){
            if(sum + nums[i] > nums[i]){
                sum = sum+nums[i];
            }else{
                sum = nums[i];
            }
            if(sum > res){
                res = sum;
            }
        }
        return res;
    }
}
// @lc code=end

