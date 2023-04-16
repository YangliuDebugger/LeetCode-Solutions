# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterate 2 passes
        d = {}

        def iterate1(node, depth):
            if not node:
                return
            if depth not in d:
                d[depth] = 0
            d[depth] += node.val
            iterate1(node.left, depth + 1)
            iterate1(node.right, depth + 1)

        iterate1(root, 0)

        def iterate2(node, bro_sum, depth):
            if not node:
                return
            node.val = d[depth] - bro_sum
            ss = 0
            if node.left:
                ss += node.left.val
            if node.right:
                ss += node.right.val
            iterate2(node.left, ss, depth + 1)
            iterate2(node.right, ss, depth + 1)

        iterate2(root, root.val, 0)
        return root