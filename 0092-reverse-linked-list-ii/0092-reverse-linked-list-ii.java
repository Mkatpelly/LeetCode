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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) return head;
        ListNode dummy = new ListNode(0, head);
        ListNode leftPrev = dummy;
        for (int i = 1; i < left; i++) {
            leftPrev = leftPrev.next;
        }
        ListNode start = leftPrev.next;
        ListNode current = start.next;

        for (int i = 0; i < right - left; i++) {
            start.next = current.next;
            current.next = leftPrev.next;
            leftPrev.next = current;
            current = start.next;
        }
        return dummy.next;
    }
}