class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.cnt = 0
        m, n = len(grid), len(grid[0])
        start = [-1, -1]
        end = [-1, -1]
        path_len = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    path_len += 1
                    continue
                if grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == 2:
                    end = [i, j]

        def dfs(node, k):
            # print(node, k)
            x, y = node
            grid[x][y] = -1
            for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    if grid[nx][ny] == 2:
                        if k == path_len - 1:
                            self.cnt += 1
                    else:
                        dfs([nx, ny], k + 1)
            grid[x][y] = 0

        dfs(start, 1)
        return self.cnt


