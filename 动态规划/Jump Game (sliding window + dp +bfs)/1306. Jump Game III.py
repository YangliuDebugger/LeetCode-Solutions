class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS + visit
        from queue import Queue
        q = Queue()
        visit = [0] * len(arr)
        visit[start] = 1
        q.put(start)
        while not q.empty():
            x = q.get()
            if arr[x] == 0:
                return True
            if x + arr[x] < len(arr) and visit[x + arr[x]] == 0:
                q.put(x + arr[x])
                visit[x + arr[x]] = 1
            if x - arr[x] >= 0 and visit[x - arr[x]] == 0:
                q.put(x - arr[x])
                visit[x - arr[x]] = 1
        return False

