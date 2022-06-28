from typing import List


class TreeNode:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # 数据规模只有1000， 甚至可以枚举移除哪两条边，还有如何高效的计算连通块里面所有元素的亦或
        # 应该是在树上进行DFS遍历
        n = len(nums)
        L = [[] for i in range(n)]
        for i, j in edges:
            L[i].append(j)
            L[j].append(i)

        # set 0 as the root
        self.D = {}
        self.D[0] = [TreeNode(nums[0], L[0]), 0, set()]  # tree node, XOR sum, parents set()

        # build tree with dfs
        def dfs(idx):
            total_sum = nums[idx]
            for child_idx in self.D[idx][0].children:
                # build tree
                if child_idx in self.D[idx][2]:
                    continue
                self.D[child_idx] = [TreeNode(nums[child_idx], L[child_idx]), 0, self.D[idx][2] | {idx}]
                children_sum = dfs(child_idx)
                total_sum = total_sum ^ children_sum
            self.D[idx][1] = total_sum
            return self.D[idx][1]

        dfs(0)
        global_min = 10 ** 10
        for idx_1 in range(n - 1):
            x, y = edges[idx_1]
            if x in self.D[y][2]:
                root1 = y
            else:
                root1 = x
            for idx_2 in range(idx_1 + 1, n - 1):
                x, y = edges[idx_2]
                if x in self.D[y][2]:
                    root2 = y
                else:
                    root2 = x
                if root1 in self.D[root2][2]:
                    xorsum = [self.D[root2][1], self.D[root1][1] ^ self.D[root2][1], self.D[0][1] ^ self.D[root1][1]]
                elif root2 in self.D[root1][2]:
                    xorsum = [self.D[root1][1], self.D[root1][1] ^ self.D[root2][1], self.D[0][1] ^ self.D[root2][1]]
                else:
                    xorsum = [self.D[root2][1], self.D[root1][1], self.D[0][1] ^ self.D[root1][1] ^ self.D[root2][1]]
                xorsum.sort()
                global_min = min(global_min, xorsum[-1] - xorsum[0])
        return global_min

solution = Solution()
print(solution.minimumScore([7,26,21,15,32], [[4,1],[0,4],[4,2],[2,3]]))