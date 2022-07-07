# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        from queue import Queue
        L = [root.val]
        d = {root.val: [root, None]}
        while True:
            tL = []
            td = {}
            for i in L:
                if d[i][0].left:
                    tL.append(d[i][0].left.val)
                    td[d[i][0].left.val] = [d[i][0].left, d[i][0]]
                if d[i][0].right:
                    tL.append(d[i][0].right.val)
                    td[d[i][0].right.val] = [d[i][0].right, d[i][0]]
                    if d[i][0].right.val in d:
                        if d[i][1].left == d[i][0]:
                            d[i][1].left = None
                        else:
                            d[i][1].right = None
                        return root
            d = td
            L = tL


