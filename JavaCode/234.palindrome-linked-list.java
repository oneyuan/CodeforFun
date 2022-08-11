import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode id=234 lang=java
 *
 * [234] Palindrome Linked List
 *
 * https://leetcode.com/problems/palindrome-linked-list/description/
 *
 * algorithms
 * Easy (42.95%)
 * Likes:    10299
 * Dislikes: 618
 * Total Accepted:    1.1M
 * Total Submissions: 2.3M
 * Testcase Example:  '[1,2,2,1]'
 *
 * Given the head of a singly linked list, return true if it is a
 * palindrome.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: head = [1,2,2,1]
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: head = [1,2]
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the list is in the range [1, 10^5].
 * 0 <= Node.val <= 9
 * 
 * 
 * 
 * Follow up: Could you do it in O(n) time and O(1) space?
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head == null){
            return true;
        }
        ListNode slow = head;
        ListNode fast = head;
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
            // in case there were circles
            if(slow == fast){
                return false;
            }
        }
        fast = reverse(slow);
        while(head != null){
            if(head.val != fast.val){
                return false;
            }
            head = head.next;
            fast = fast.next;
        }
        return true;
    }

    public ListNode reverse(ListNode head){
        ListNode dummyHead = null;
        ListNode cur = head;
        while(cur != null){
            ListNode next = cur.next;
            cur.next = dummyHead;
            dummyHead = cur;
            cur = next;
        }
        return dummyHead;
    }

    public boolean isPalindrome0(ListNode head) {
        if(head == null){
            return true;
        }
        List<ListNode> list = new ArrayList<>();
        ListNode cur = head;
        while(cur != null){
            ListNode curNode = cur;
            list.add(curNode);
            cur = cur.next;
        }
        int n = list.size();
        int j = n - 1;
        for(int i = 0; i <= j; i++, j--){
            if(list.get(i).val != list.get(j).val){
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

