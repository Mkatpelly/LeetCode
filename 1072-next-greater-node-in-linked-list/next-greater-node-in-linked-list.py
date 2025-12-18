# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        n = len(vals)
        ans = [0] * n
        stack = []  # will store indices with decreasing vals

        # 2) Monotonic stack from left to right
        for i, v in enumerate(vals):
            # while current value is greater than value at stack top,
            # it's the "next greater" for that earlier index
            while stack and vals[stack[-1]] < v:
                idx = stack.pop()
                ans[idx] = v
            stack.append(i)

        # remaining indices in stack have no next greater → stay 0
        return ans