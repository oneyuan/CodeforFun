import java.util.Comparator;
import java.util.PriorityQueue;

/*
 * @lc app=leetcode id=239 lang=java
 *
 * [239] Sliding Window Maximum
 *
 * https://leetcode.com/problems/sliding-window-maximum/description/
 *
 * algorithms
 * Hard (45.08%)
 * Likes:    11230
 * Dislikes: 373
 * Total Accepted:    622.4K
 * Total Submissions: 1.3M
 * Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
 *
 * You are given an array of integers nums, there is a sliding window of size k
 * which is moving from the very left of the array to the very right. You can
 * only see the k numbers in the window. Each time the sliding window moves
 * right by one position.
 * 
 * Return the max sliding window.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
 * Output: [3,3,5,5,6,7]
 * Explanation: 
 * Window position                Max
 * ---------------               -----
 * [1  3  -1] -3  5  3  6  7       3
 * ⁠1 [3  -1  -3] 5  3  6  7       3
 * ⁠1  3 [-1  -3  5] 3  6  7       5
 * ⁠1  3  -1 [-3  5  3] 6  7       5
 * ⁠1  3  -1  -3 [5  3  6] 7       6
 * ⁠1  3  -1  -3  5 [3  6  7]      7
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1], k = 1
 * Output: [1]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 * 1 <= k <= nums.length
 * 
 * 
 */

// @lc code=start
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(new Comparator<int[]>(){
            public int compare(int[] pair1, int[] pair2){
                return pair1[0] != pair2[0] ? pair2[0] - pair1[0] : pair1[1] - pair2[1];
            }
        });
        for(int i = 0; i < k; i++){
            pq.add(new int[]{nums[i], i});
        }
        int[] res = new int[n-k+1];
        res[0] = pq.peek()[0];
        for(int j = k; j < n; j++){
            pq.offer(new int[]{nums[j], j});
            while(pq.peek()[1] <= j - k){
                pq.poll();
            }
            res[j-k+1] = pq.peek()[0];
        }
        return res;
    }

    public int[] maxSlidingWindow1(int[] nums, int k) {
        int len = nums.length;
        int[] left = new int[len];
        int[] right = new int[len];
        int[] res = new int[len-k+1];
        int i = 0;
        while(i < len){
            int l = i;
            int r = Math.min(i+k-1, len-1);
            left[l] = nums[l];
            right[r] = nums[r];
            for(int j = 1; j < r-l+1; j++){
                left[i+j] = Math.max(left[i+j-1], nums[i+j]);
                right[r-j] = Math.max(right[r-j+1], nums[r-j]);
            }
            i+=k;
        }
        for(int m = 0; m < len-k+1; m++){
            res[m] = Math.max(right[m], left[m+k-1]);
        }
        return res;
    }
}
// @lc code=end

