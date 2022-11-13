class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # BFS
        from collections import deque
        x, y = abs(x), abs(y)
        q = deque([(0,0,0)])
        visit = set()
        while q:
            tx,ty,step = q.popleft()
            if x==tx and y==ty:
                return step
            for dx, dy in [[1,-2], [1, 2], [-1, 2], [2,-1], [2,1], [-2, 1]]:
                nx, ny = tx+dx, ty+dy
                if -1<=nx and -1<=ny and (nx, ny) not in visit:
                    visit.add((nx, ny))
                    q.append((nx,ny,step+1))