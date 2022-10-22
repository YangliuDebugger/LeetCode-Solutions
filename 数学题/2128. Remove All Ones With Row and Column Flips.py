class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        # 对于每一行每一列来说，只有不翻翻一次2种选择
        # 对于已经是1的格子，要么都不翻，要么翻两次，行列各一次
        # 分两种情况检验，翻第一行，和不翻第一行, 只用检验第一种情况，第二种情况应该全是0
        # 可以一起检验

        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n

        row[0] = 0
        for i in range(n):
            col[i] = 1 - grid[0][i]
        for i in range(m):
            row[i] = (grid[i][0] + col[0] + 1) % 2
        print(row, col)
        cnt = 0
        for i in range(m):
            for j in range(n):
                cnt += (grid[i][j] + row[i] + col[j]) % 2
        return cnt == 0 or cnt == m * n