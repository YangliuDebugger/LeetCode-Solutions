from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # BFS
        m, n = len(grid), len(grid[0])
        visited = [[-1] * n for _ in range(m)]
        visited[0][0] = k
        q = deque()
        q.append([0, 0, 0, k])
        while len(q) > 0:
            x = q.popleft()
            if x[0] == m - 1 and x[1] == n - 1:
                return x[2]
            for steps in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                di, dj = steps
                ni, nj = x[0] + di, x[1] + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 0:
                        if visited[ni][nj] < x[3]:
                            visited[ni][nj] = x[3]
                            q.append([ni, nj, x[2] + 1, x[3]])
                    else:
                        if visited[ni][nj] + 1 < x[3]:
                            visited[ni][nj] = x[3] - 1
                            q.append([ni, nj, x[2] + 1, x[3] - 1])
        return -1


