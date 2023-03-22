# https://www.1point3acres.com/bbs/thread-957371-1-1.html

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # find medium of x and y
        m, n = len(grid), len(grid[0])
        cnt = 0
        x = []
        y = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        y.sort()
        bestx, besty = x[len(x)//2], y[len(y)//2]
        dis = 0
        for i, j in zip(x, y):
            dis += abs(i-bestx) + abs(j-besty)
        return dis