# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverseLL(self, head):

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def addTwoNumbers(self, l1, l2):

        l1 = self.reverseLL(l1)
        l2 = self.reverseLL(l2)


        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val = carry

            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            curr = curr.next

        return self.reverseLL(dummy.next)
        