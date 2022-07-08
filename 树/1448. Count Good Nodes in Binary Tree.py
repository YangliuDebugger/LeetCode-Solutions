# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0

        def dfs(node, maxx):
            if node:
                if node.val >= maxx:
                    self.cnt += 1
                dfs(node.left, max(node.val, maxx))
                dfs(node.right, max(node.val, maxx))

        dfs(root, -100000)
        return self.cnt