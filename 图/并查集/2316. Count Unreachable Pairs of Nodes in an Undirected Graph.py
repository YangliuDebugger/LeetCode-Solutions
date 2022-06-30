class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # union find
        parent = [i for i in range(n)]

        def findparent(i):
            if parent[i] != i:
                parent[i] = findparent(parent[i])
            return parent[i]

        cnt = 0
        for i, j in edges:
            pi = findparent(i)
            pj = findparent(j)
            parent[pj] = pi

        d = {}
        for i in parent:
            pi = findparent(i)
            if pi not in d:
                d[pi] = 0
            d[pi] += 1

        for p in d:
            cnt += d[p] * (n - d[p])
        return cnt // 2