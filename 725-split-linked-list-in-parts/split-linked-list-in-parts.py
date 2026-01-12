# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # 2) Compute base size and number of longer parts
        base, extra = divmod(n, k)

        # 3) Split into k parts
        res: List[Optional[ListNode]] = [None] * k
        curr = head

        for i in range(k):
            if not curr:
                res[i] = None
                continue

            # head of current part
            res[i] = curr
            # size of this part
            part_size = base + (1 if i < extra else 0)

            # move to the last node of this part
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next

            # cut and move to next part
            if curr:
                nxt = curr.next
                curr.next = None
                curr = nxt

        return res