/*
 * @lc app=leetcode id=1043 lang=java
 *
 * [1043] Partition Array for Maximum Sum
 *
 * https://leetcode.com/problems/partition-array-for-maximum-sum/description/
 *
 * algorithms
 * Medium (72.44%)
 * Likes:    4264
 * Dislikes: 340
 * Total Accepted:    136.2K
 * Total Submissions: 180.9K
 * Testcase Example:  '[1,15,7,9,2,5,10]\n3'
 *
 * Given an integer array arr, partition the array into (contiguous) subarrays
 * of length at most k. After partitioning, each subarray has their values
 * changed to become the maximum value of that subarray.
 * 
 * Return the largest sum of the given array after partitioning. Test cases are
 * generated so that the answer fits in a 32-bit integer.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: arr = [1,15,7,9,2,5,10], k = 3
 * Output: 84
 * Explanation: arr becomes [15,15,15,9,10,10,10]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
 * Output: 83
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: arr = [1], k = 1
 * Output: 1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= arr.length <= 500
 * 0 <= arr[i] <= 10^9
 * 1 <= k <= arr.length
 * 
 * 
 */

// @lc code=start
class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        int len = arr.length;
        int[] res = new int[len + 1];
        for(int i = 1; i <= len; i++ ) {
            int maxValue = arr[i-1];
            for(int j = i-1; j >=0 && j >= i-k; j--) {
                res[i] = Math.max(res[i], res[j] + maxValue * (i-j));
                if( j > 0) {
                    maxValue = Math.max(maxValue, arr[j-1]);
                }
            }
        }
        return res[len];
    }
}
// @lc code=end

