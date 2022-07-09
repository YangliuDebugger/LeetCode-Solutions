# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.left and node.right:
                a = dfs(node.left)
                b = dfs(node.right)
                if node.val == 2:
                    return a or b
                return a and b
            else:
                if node.val == 0:
                    return False
                return True

        return dfs(root)
