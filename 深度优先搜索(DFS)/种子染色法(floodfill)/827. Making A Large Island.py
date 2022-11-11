class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # floodfill
        m, n = len(grid), len(grid[0])
        self.D = {}
        # pitfall 1: no 1s
        self.best = 1

        def floodfill(x, y, seed):
            self.D[seed] += 1
            grid[x][y] = seed
            for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    floodfill(nx, ny, seed)

        seed = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    seed += 1
                    self.D[seed] = 0
                    floodfill(i, j, seed)
                    # pitfall 2: no 0s
                    self.best = max(self.best, self.D[seed])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    L = {}
                    cnt = 1
                    for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 1:
                            L[grid[nx][ny]] = self.D[grid[nx][ny]]
                    for x in L:
                        cnt += L[x]
                    self.best = max(self.best, cnt)

        return self.best
