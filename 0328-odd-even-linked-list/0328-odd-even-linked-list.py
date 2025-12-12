# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # remember start of even list

        # Re-link nodes so that odds followed by evens
        while even and even.next:
            odd.next = even.next     # link current odd to next odd
            odd = odd.next           # move odd pointer

            even.next = odd.next     # link current even to next even
            even = even.next         # move even pointer

        # attach even list after odd list
        odd.next = even_head
        return head