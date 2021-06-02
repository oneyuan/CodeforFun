import java.util.Stack;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode id=112 lang=java
 *
 * [112] Path Sum
 *
 * https://leetcode.com/problems/path-sum/description/
 *
 * algorithms
 * Easy (42.90%)
 * Likes:    3206
 * Dislikes: 620
 * Total Accepted:    624.6K
 * Total Submissions: 1.5M
 * Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
 *
 * Given the root of a binary tree and an integer targetSum, return true if the
 * tree has a root-to-leaf path such that adding up all the values along the
 * path equals targetSum.
 * 
 * A leaf is a node with no children.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: root = [1,2,3], targetSum = 5
 * Output: false
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: root = [1,2], targetSum = 0
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree is in the range [0, 5000].
 * -1000 <= Node.val <= 1000
 * -1000 <= targetSum <= 1000
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null){
            return false;
        }
        int res = 0;
        Stack<TreeNode> s = new Stack<>();
        Stack<Integer> si = new Stack<>();
        s.push(root);
        si.push(root.val);
        while(!s.isEmpty()){
            TreeNode cur = s.pop();
            Integer i = si.pop();
            if(cur.right != null){
                s.push(cur.right);
                si.push(i + cur.right.val);
            }
            if(cur.left != null){
                s.push(cur.left);
                si.push(i + cur.left.val);
            }
            if(cur.left == null && cur.right == null && i == targetSum){
                return true;
            }
        }
        return false;
    }
}
// @lc code=end

