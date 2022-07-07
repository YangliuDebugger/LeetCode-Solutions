# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        def dfs(node):
            total, cnt = node.val, 1
            if node.left:
                a, b = dfs(node.left)
                total += a
                cnt += b
            if node.right:
                a, b = dfs(node.right)
                total += a
                cnt += b
            if node.val == total // cnt:
                self.cnt += 1
            return total, cnt
        dfs(root)
        return self.cnt