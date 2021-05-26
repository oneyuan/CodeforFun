/*
 * @lc app=leetcode id=111 lang=java
 *
 * [111] Minimum Depth of Binary Tree
 *
 * https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
 *
 * algorithms
 * Easy (40.13%)
 * Likes:    2464
 * Dislikes: 832
 * Total Accepted:    563.6K
 * Total Submissions: 1.4M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given a binary tree, find its minimum depth.
 * 
 * The minimum depth is the number of nodes along the shortest path from the
 * root node down to the nearest leaf node.
 * 
 * Note: A leaf is a node with no children.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root = [3,9,20,null,null,15,7]
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: root = [2,null,3,null,4,null,5,null,6]
 * Output: 5
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree is in the range [0, 10^5].
 * -1000 <= Node.val <= 1000
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
    public int minDepth(TreeNode root) {
        //DFS not so good when it comes to height BFS may be the better choice
        if(root == null){
            return 0;
        }
        int tmp;
        int res = Integer.MAX_VALUE;
        Stack<TreeNode> s = new Stack<>();
        Stack<Integer> ss = new Stack<>();
        s.push(root);
        ss.push(1);
        while(!s.isEmpty()){
            TreeNode cur = s.pop();
            tmp = ss.pop();
            if(cur.left == null && cur.right == null && tmp < res){
                res = tmp;
            }
            if(cur.right != null){
                s.push(cur.right);
                ss.push(tmp + 1);
            }
            if(cur.left != null){
                s.push(cur.left);
                ss.push(tmp + 1);
            } 
        }
        return res;
    }
}
// @lc code=end

