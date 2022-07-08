# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.maxdepth = 0
        self.ans = None

        def dfs(node, depth):
            if not node:
                if depth > self.maxdepth:
                    self.maxdepth = depth
                return depth
            max_depth1 = dfs(node.left, depth + 1)
            max_depth2 = dfs(node.right, depth + 1)
            if max_depth1 == max_depth2:
                # 利用了深度优先的特点
                if max_depth1 == self.maxdepth:
                    self.ans = node
            return max(max_depth1, max_depth2)

        dfs(root, 0)
        return self.ans
