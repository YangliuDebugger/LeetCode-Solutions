import collections

class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        d = collections.defaultdict(int)
        for q in queries:
            d[q] += 1

        self.cnt = 0

        def DFS(i, cnt):
            if i > n:
                return
            cnt += d[i]
            if cnt % 2 == 1:
                self.cnt += 1
            DFS(2 * i, cnt)
            DFS(2 * i + 1, cnt)

        DFS(1, 0)
        return self.cnt