# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # layer by layer
        L = [root]
        d = 0
        while L:
            d += 1
            tL = []
            for idx, i in enumerate(L):
                tL.append(i.left)
                tL.append(i.right)
                if d % 2 == 0 and idx < len(L)//2:
                    i.val, L[len(L)-idx-1].val = L[len(L)-idx-1].val, i.val
            if tL[0] is None:
                break
            L = tL
        return root
