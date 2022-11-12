class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    q.append((i, j, 0))

        while q:
            x, y, step = q.popleft()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == '#':
                        return step + 1
                    elif grid[nx][ny] == 'O':
                        q.append((nx, ny, step + 1))
                        grid[nx][ny] = 'X'
        return -1


