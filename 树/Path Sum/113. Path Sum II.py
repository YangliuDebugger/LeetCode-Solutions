# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.path = []

        def dfs(node, cursum):
            if not node:
                return
            self.path.append(node.val)
            if cursum + node.val == targetSum:
                if node.left is None and node.right is None:
                    res.append(self.path[:])
            dfs(node.left, cursum + node.val)
            dfs(node.right, cursum + node.val)
            self.path.pop()

        dfs(root, 0)
        return res