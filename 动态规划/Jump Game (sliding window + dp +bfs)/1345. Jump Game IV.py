class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # 还是BFS就可以啊，用不到dp
        from queue import Queue
        from collections import defaultdict
        q = Queue()
        visit = [0] * len(arr)
        q.put((0, 0))
        visit[0] = 1
        d = defaultdict(list)
        for idx, i in enumerate(arr):
            d[i].append(idx)
        while not q.empty():
            x, step = q.get()
            if x == len(arr) - 1:
                return step
            if x - 1 >= 0 and visit[x - 1] == 0:
                q.put((x - 1, step + 1))
                visit[x - 1] = 1
            if visit[x + 1] == 0:
                q.put((x + 1, step + 1))
                visit[x + 1] = 1
            for xx in d[arr[x]]:
                if xx != x:
                    q.put((xx, step + 1))
                    visit[xx] = 1
            d[arr[x]] = []
