/*
 * @lc app=leetcode id=322 lang=java
 *
 * [322] Coin Change
 *
 * https://leetcode.com/problems/coin-change/description/
 *
 * algorithms
 * Medium (38.14%)
 * Likes:    12182
 * Dislikes: 277
 * Total Accepted:    1M
 * Total Submissions: 2.6M
 * Testcase Example:  '[1,2,5]\n11'
 *
 * You are given an integer array coins representing coins of different
 * denominations and an integer amount representing a total amount of money.
 * 
 * Return the fewest number of coins that you need to make up that amount. If
 * that amount of money cannot be made up by any combination of the coins,
 * return -1.
 * 
 * You may assume that you have an infinite number of each kind of coin.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: coins = [1,2,5], amount = 11
 * Output: 3
 * Explanation: 11 = 5 + 5 + 1
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: coins = [2], amount = 3
 * Output: -1
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: coins = [1], amount = 0
 * Output: 0
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= coins.length <= 12
 * 1 <= coins[i] <= 2^31 - 1
 * 0 <= amount <= 10^4
 * 
 * 
 */

// @lc code=start
class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount < 1){
            return 0;
        }
        return dynamicProgram(coins, new int[amount], amount);
    }
    
    public int dynamicProgram(int[] coins, int[] num, int remain){
        if(remain < 0){
            return -1;
        }
        if(remain == 0){
            return 0;
        }
        if(num[remain-1] != 0){
            return num[remain-1];
        }
        int min = Integer.MAX_VALUE;
        for(int i : coins){
            int res = dynamicProgram(coins, num, remain-i)+1;
            if(res > 0 && res < min){
                min = res;
            }
        }
        if(Integer.MAX_VALUE == min){
            num[remain-1] = -1;
        }else{
            num[remain-1] = min;
        }
        return num[remain-1];
    }

}
// @lc code=end

