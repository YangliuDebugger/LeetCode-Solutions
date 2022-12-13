class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # heap problem
        import heapq
        L = [(grid[0][0], 0, 0)]
        m, n = len(grid), len(grid[0])
        visit = [[0] * n for _ in range(m)]
        visit[0][0] = 1
        cnt = 0

        queries = [(v, idx) for idx, v in enumerate(queries)]
        queries.sort()
        res = []
        q_idx = 0

        while L and q_idx < len(queries):

            level = L[0][0] + 1
            while q_idx < len(queries) and queries[q_idx][0] < level:
                res.append((queries[q_idx][1], cnt))
                q_idx += 1

            stack = []
            while (L and L[0][0] < level) or stack:
                if stack:
                    _, x, y = stack.pop()
                else:
                    _, x, y = heapq.heappop(L)
                cnt += 1
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        if grid[nx][ny] < level:
                            stack.append((0, nx, ny))
                        else:
                            heapq.heappush(L, (grid[nx][ny], nx, ny))

        while q_idx < len(queries):
            res.append((queries[q_idx][1], cnt))
            q_idx += 1

        res.sort()
        return [v for idx, v in res]




