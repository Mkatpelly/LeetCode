# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        for _ in range(k - 1):
            first = first.next
        
        # Step 2: find the k-th node from the end
        second = head
        runner = first.next
        while runner:
            runner = runner.next
            second = second.next
        
        # Step 3: swap values
        first.val, second.val = second.val, first.val
        
        return head
