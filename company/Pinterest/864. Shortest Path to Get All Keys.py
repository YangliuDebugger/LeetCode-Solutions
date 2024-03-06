from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        num_keys = 1
        for i in range(m):
            for j in range(n):
                num_keys = max(num_keys, ord(grid[i][j]) - ord('a') + 1)
                if grid[i][j] == '@':
                    start_x, start_y = i, j
        end_key_state = 2 ** num_keys - 1

        # BFS with state mem
        # state definition [row, col], value is key_bit
        visit = {}
        q = deque()
        q.append([start_x, start_y, 0, 0])
        visit[(start_x, start_y)] = 0
        while q:
            x, y, key_bits, step = q.popleft()
            # print(x, y, key_bits, step)
            if key_bits == end_key_state:
                return step
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                    if (nx, ny) in visit and visit[(nx, ny)] | key_bits == visit[(nx, ny)]: # visit before with more keys
                        continue
                    if grid[nx][ny] == '.' or grid[nx][ny] == '@':
                        visit[(nx, ny)] = key_bits
                        q.append((nx, ny, key_bits, step+1))
                    elif 'a' <= grid[nx][ny] <= 'z':
                        n_key_bits = key_bits | 2 ** (ord(grid[nx][ny]) - ord('a'))
                        visit[(nx, ny)] = n_key_bits
                        q.append((nx, ny, n_key_bits, step + 1))
                    else:  # lock
                        lock_bit = 2 ** (ord(grid[nx][ny]) - ord('A'))
                        if key_bits & lock_bit > 0:
                            visit[(nx, ny)] = key_bits
                            q.append((nx, ny, key_bits, step + 1))
        return -1

