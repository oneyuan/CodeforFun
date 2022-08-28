import java.util.Random;

/*
 * @lc app=leetcode id=215 lang=java
 *
 * [215] Kth Largest Element in an Array
 *
 * https://leetcode.com/problems/kth-largest-element-in-an-array/description/
 *
 * algorithms
 * Medium (59.71%)
 * Likes:    11572
 * Dislikes: 582
 * Total Accepted:    1.5M
 * Total Submissions: 2.3M
 * Testcase Example:  '[3,2,1,5,6,4]\n2'
 *
 * Given an integer array nums and an integer k, return the k^th largest
 * element in the array.
 * 
 * Note that it is the k^th largest element in the sorted order, not the k^th
 * distinct element.
 * 
 * You must solve it in O(n) time complexity.
 * 
 * 
 * Example 1:
 * Input: nums = [3,2,1,5,6,4], k = 2
 * Output: 5
 * Example 2:
 * Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
 * Output: 4
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= k <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 * 
 * 
 */

// @lc code=start
class Solution {

    Random random = new Random();

    public int findKthLargest(int[] nums, int k) {
        // if high is the length of array, when random the int number 
        // use high-low as the bound
        return quickSelect(nums, 0, nums.length, nums.length - k);
    }

    public void swap(int[] nums, int i, int j){
        if(i == j){
            return;
        }
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    public int partition(int[] nums, int low, int high){
        int pivot = nums[high-1];
        int i = low;
        for(int j = low; j < high - 1; j++){
            // use equal to avoid the pivot count is not the only child. hhhh
            if(nums[j] <= pivot){
                swap(nums, i, j);
                i++;
            }
        }
        swap(nums, i, high-1);
        return i;
    }

    public int quickSelect(int[] nums, int low, int high, int pivotIndex){
        int i = random.nextInt(high - low) + low;
        // swap the ramdom pivot with the last number, it change back to quick
        // sort with last element as pivot
        swap(nums, i, high-1);
        int p = partition(nums, low, high);
        if(p == pivotIndex){
            return nums[p];
        }else{
            if(p < pivotIndex){
                return quickSelect(nums, p, high, pivotIndex);
            }else{
                return quickSelect(nums, low, p, pivotIndex);
            }
        }
    }
}
// @lc code=end

