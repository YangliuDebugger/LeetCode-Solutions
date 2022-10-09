# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        d = {}

        def dfs(node):
            if node:
                d[node.val] = node
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        m = TreeNode()
        f = m
        for i in sorted(d.keys()):
            f.left = None
            f.right = d[i]
            f = f.right
        f.left = None
        return m.right