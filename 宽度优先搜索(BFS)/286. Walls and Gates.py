class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # BFS
        m, n = len(rooms), len(rooms[0])
        L = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    L.append([i, j])
        steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while L:
            tL = []
            for x, y in L:
                for dx, dy in steps:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] > rooms[x][y]+1:
                        rooms[nx][ny] = rooms[x][y] + 1
                        tL.append([nx, ny])
            L = tL
