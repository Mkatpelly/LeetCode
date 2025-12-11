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
    public ListNode sortList(ListNode head) {
          if (head == null || head.next == null) {
            return head;
        }

        // Step 1: Split the linked list into two halves
        ListNode mid = getMiddle(head);
        ListNode left = head;
        ListNode right = mid.next;
        mid.next = null; // Break the link to split the list

        // Step 2: Sort each half recursively
        left = sortList(left);
        right = sortList(right);

        // Step 3: Merge the two sorted halves
        return merge(left, right);
    }

    // Helper method to find the middle of the list
    private ListNode getMiddle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    // Helper method to merge two sorted lists
    private ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0); // Dummy node to simplify merging
        ListNode current = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
        }

        // Append any remaining nodes
        if (l1 != null) {
            current.next = l1;
        }
        if (l2 != null) {
            current.next = l2;
        }

        return dummy.next;
    }
    }
