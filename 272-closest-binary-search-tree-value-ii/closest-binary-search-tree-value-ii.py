class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if k == 0 or not root: return []
        stk, cur, result, count = [], root, [], 0
        #inorder traversal of the tree
        while len(stk) != 0 or cur != None:
            if cur != None:
                stk.append(cur)
                cur = cur.left
            else:
                cur = stk.pop()
                #if the window smaller than k, we just append the element
                if count < k:
                    result.append(cur.val)
                #if not, we check whether element(first one in the window or the current one) is closer to the target
                else:
                    if abs(result[0] - target) > abs(cur.val - target):
                        result.pop(0)
                        result.append(cur.val)
                    else:
                        break
                count += 1
                cur = cur.right
        return result