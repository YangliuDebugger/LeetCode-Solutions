class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        l, m, n = len(mat1), len(mat1[0]), len(mat2[0])
        ans = [[0] * n for _ in range(l)]
        for i in range(l):
            for j in range(m):
                if mat1[i][j] != 0:
                    for k in range(n):
                        ans[i][k] += mat1[i][j] * mat2[j][k]
        return ans