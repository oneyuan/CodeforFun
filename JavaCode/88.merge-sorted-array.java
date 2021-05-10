/*
 * @lc app=leetcode id=88 lang=java
 *
 * [88] Merge Sorted Array
 *
 * https://leetcode.com/problems/merge-sorted-array/description/
 *
 * algorithms
 * Easy (40.77%)
 * Likes:    3759
 * Dislikes: 5320
 * Total Accepted:    870.5K
 * Total Submissions: 2.1M
 * Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
 *
 * Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
 * one sorted array.
 * 
 * The number of elements initialized in nums1 and nums2 are m and n
 * respectively. You may assume that nums1 has a size equal to m + n such that
 * it has enough space to hold additional elements from nums2.
 * 
 * 
 * Example 1:
 * Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
 * Output: [1,2,2,3,5,6]
 * Example 2:
 * Input: nums1 = [1], m = 1, nums2 = [], n = 0
 * Output: [1]
 * 
 * 
 * Constraints:
 * 
 * 
 * nums1.length == m + n
 * nums2.length == n
 * 0 <= m, n <= 200
 * 1 <= m + n <= 200
 * -10^9 <= nums1[i], nums2[i] <= 10^9
 * 
 * 
 * 
 * Follow up: Can you come up with an algorithm that runs in O(m + n) time?
 */

// @lc code=start
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if(n==0) return;
        if(m==0){
            for(int i = 0; i < n; i++){
                nums1[i] = nums2[i];
            }
            return;
        }
        int[] tmp = new int[m];
        for(int i = 0; i < m; i++){
            tmp[i] = nums1[i];
        }
        int j = 0;
        int point1, point2;
        point1 = point2 = 0;
        while(point1 + point2 < m+n){
            if(tmp[point1] < nums2[point2]){
                nums1[j]=tmp[point1];
                point1++;
            }else{
                nums1[j] = nums2[point2];
                point2++;
            }
            j++;
            if(point1 == m){
                while(j < m+n){
                    nums1[j] = nums2[point2];
                    point2++;
                    j++;
                }
            }
            if(point2 == n){
                while(j<m+n){
                    nums1[j] = tmp[point1];
                    point1++;
                    j++;
                }
            }
        }
    }
}
// @lc code=end

