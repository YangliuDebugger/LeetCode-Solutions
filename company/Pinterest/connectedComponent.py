
grid = []
def isSameObject(i,j,x,y):
    if grid[i][j] == grid[x][y] and grid[i][j] != "":
        return True
    return False

def countisland():
    m, n = len(grid), len(grid[0])
    visit = [[0] * n for _ in range(m)]

    def floodfill(x, y):
        visit[x][y] = 1
        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and isSameObject(x, y, nx, ny) and not visit[nx][ny]:
                floodfill(nx, ny)

    cnt = 0
    for i in range(m):
        for j in range(n):
            if isSameObject(i, j, i, j) and not visit[i][j]:
                cnt += 1
                floodfill(i, j)

    return cnt

grid = [["" ,"x", "y"], ["z", "x", "y"], ["", "x",""]]
print(countisland())