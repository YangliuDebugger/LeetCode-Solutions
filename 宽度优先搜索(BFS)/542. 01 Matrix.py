class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        q = deque()
        m, n = len(mat), len(mat[0])
        res = [[0] * n for i in range(m)]
        steps = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visit = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    for di, dj in steps:
                        ni, nj = i + di, j + dj
                        if 0<=ni<m and 0<=nj<n and mat[ni][nj] == 1:
                            res[ni][nj] = 1
                            visit[ni][nj] = 1
                            q.append((ni, nj, 1))
        while q:
            i, j, depth = q.popleft()
            for di, dj in steps:
                ni, nj = i + di, j + dj
                if 0<=ni<m and 0<=nj<n and mat[ni][nj] == 1 and visit[ni][nj] == 0:
                    res[ni][nj] = depth+1
                    visit[ni][nj] = 1
                    q.append((ni, nj, depth+1))

        return res


