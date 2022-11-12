# 两种解法，关键是BFS多记录一个状态就是目前用了多少elimation

class Solution:
    def shortestPath_naive(self, grid: List[List[int]], k: int) -> int:
        # BFS with one more state
        from collections import deque
        q = deque()
        m, n = len(grid), len(grid[0])
        visit = set()
        q.append((0,0,0,0))
        visit.add((0,0,0))
        while q:
            x, y, elimation, step = q.popleft()
            # print(x,y,elimation,step)
            if x == m-1 and y == n-1:
                return step
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0<=nx<m and 0<=ny<n:
                    if elimation+grid[nx][ny] <= k and (nx,ny,elimation+grid[nx][ny]) not in visit:
                        visit.add((nx,ny,elimation+grid[nx][ny]))
                        q.append((nx,ny,elimation+grid[nx][ny],step+1))
        return -1

    # 最优化剪枝
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # BFS with one more state
        from collections import deque
        q = deque()
        m, n = len(grid), len(grid[0])
        visit = {}
        q.append((0, 0, 0, 0))
        visit[(0, 0)] = 0
        while q:
            x, y, elimation, step = q.popleft()
            # print(x,y,elimation,step)
            if x == m - 1 and y == n - 1:
                return step
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # 最优化剪枝 elimation + grid[nx][ny] < visit[(nx, ny)])
                    if elimation + grid[nx][ny] <= k and ((nx, ny) not in visit or elimation + grid[nx][ny] < visit[(nx, ny)]):
                        visit[(nx, ny)] = elimation + grid[nx][ny]
                        q.append((nx, ny, elimation + grid[nx][ny], step + 1))
        return -1

