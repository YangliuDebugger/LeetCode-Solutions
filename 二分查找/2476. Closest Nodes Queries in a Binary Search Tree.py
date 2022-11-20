# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        N = 10 ** 9
        # def findsmall(node, x):
        #     if node is None:
        #         return -N
        #     if node.val == x:
        #         return x
        #     if node.val < x:
        #         return max(node.val, findsmall(node.right, x))
        #     return findsmall(node.left, x)

        # def findbig(node, x):
        #     if node is None:
        #         return N
        #     if node.val == x:
        #         return x
        #     if node.val > x:
        #         return min(node.val, findbig(node.left, x))
        #     return findbig(node.right, x)

        # this tree might not be a balanced one
        arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        import bisect
        res = []
        print(arr)
        for i in queries:
            big, small = bisect.bisect_left(arr, i), bisect.bisect_right(arr, i)
            if big == len(arr):
                small, big = arr[-1], -1
            elif small == 0:
                small, big = -1, arr[0]
            else:
                small, big = arr[small - 1], arr[big]
            res.append([small, big])
        return res