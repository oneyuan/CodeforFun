/*
 * @lc app=leetcode id=300 lang=java
 *
 * [300] Longest Increasing Subsequence
 *
 * https://leetcode.com/problems/longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (45.24%)
 * Likes:    12910
 * Dislikes: 247
 * Total Accepted:    917.8K
 * Total Submissions: 1.8M
 * Testcase Example:  '[10,9,2,5,3,7,101,18]'
 *
 * Given an integer array nums, return the length of the longest strictly
 * increasing subsequence.
 * 
 * A subsequence is a sequence that can be derived from an array by deleting
 * some or no elements without changing the order of the remaining elements.
 * For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [10,9,2,5,3,7,101,18]
 * Output: 4
 * Explanation: The longest increasing subsequence is [2,3,7,101], therefore
 * the length is 4.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [0,1,0,3,2,3]
 * Output: 4
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [7,7,7,7,7,7,7]
 * Output: 1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 2500
 * -10^4 <= nums[i] <= 10^4
 * 
 * 
 * 
 * Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
 * complexity?
 * 
 */

// @lc code=start
class Solution {
    public int lengthOfLIS(int[] nums) {
        int len = nums.length;
        int[] dp = new int[len];
        dp[0] = 1;
        int res = Integer.MIN_VALUE;
        for(int i = 0; i < len; i++){
            dp[i] = 1;
            int j = 0;
            while(j < i){
                if(nums[j] < nums[i]){
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
                j++;
            }
            res = Math.max(res, dp[i]);
        }
        return res;
    }

    public int lengthOfLIS0(int[] nums){
        int len = nums.length;
        if(len == 0){
            return 0;
        }
        int[] dp = new int[len+1];
        dp[1] = nums[0];
        int ptr = 1;
        for(int i = 1; i < len; i++){
            if(nums[i] > dp[ptr]){
                dp[++ptr] = nums[i];
            }else{
                int l = 1, r = ptr, m = 0;
                while(l <= r){
                    int mid = (l + r) >> 1;
                    if(nums[i] > dp[mid]){
                        m = mid;
                        l = mid + 1;
                    }else{
                        r = mid - 1;
                    }
                }
                dp[m+1] = nums[i];
            }
        }
        return ptr;
    }
}
// @lc code=end

