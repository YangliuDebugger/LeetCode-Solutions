class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # BFS
        from queue import Queue
        import heapq
        L = [[] for _ in range(n)]
        for u, v, t in roads:
            L[u].append((v, t))
            L[v].append((u, t))
        cnt = [0] * n
        path = [10 ** 50] * n
        cnt[0] = 1
        path[0] = 0
        min_heap = []
        N = 10 ** 9 + 7
        indegree = [0] * n

        q = Queue()
        q.put(0)
        while not q.empty():
            current = q.get()
            for v, t in L[current]:
                if t + path[current] <= path[v]:
                    if path[v] == t + path[current]:
                        indegree[v] += 1
                    else:
                        indegree[v] = 1
                    path[v] = t + path[current]
                    heapq.heappush(min_heap, (t + path[current], v, cnt[current] % N, current))

            # print(current, min_heap, cnt)
            while min_heap:
                p, v, count, _ = heapq.heappop(min_heap)
                if p > path[v]:
                    continue
                if p == path[v]:
                    cnt[v] = (cnt[v] + count) % N
                else:
                    cnt[v] = count % N
                    path[v] = p
                indegree[v] -= 1
                if indegree[v] != 0:
                    continue
                q.put(v)
                break
        return cnt[-1]




