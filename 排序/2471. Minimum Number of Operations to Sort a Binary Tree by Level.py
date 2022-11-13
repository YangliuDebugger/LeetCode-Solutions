# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # how many swaps need to make an array sorted:
        def minswap(arr):
            # return 0
            target = sorted(arr)
            reverse = {}
            for idx, i in enumerate(arr):
                reverse[i] = idx

            idx = 0
            cnt = 0
            while idx < len(arr):
                if arr[idx] == target[idx]:
                    idx += 1
                else:
                    pos_1 = idx
                    pos_2 = reverse[target[idx]]
                    reverse[arr[idx]] = pos_2
                    arr[pos_1], arr[pos_2] = arr[pos_2], arr[pos_1]
                    cnt += 1
            return cnt

        cnt = 0
        L = [root]
        while L:
            cnt += minswap([i.val for i in L])
            tL = []
            for i in L:
                if i.left:
                    tL.append(i.left)
                if i.right:
                    tL.append(i.right)
            L = tL
        return cnt



