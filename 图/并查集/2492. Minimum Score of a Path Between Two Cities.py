class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # union find
        min_dis = [10 ** 9 + 7 for i in range(n + 1)]
        parent = [i for i in range(n + 1)]

        def findAns(node):
            if parent[node] != node:
                parent[node] = findAns(parent[node])
            return parent[node]

        for i, j, dis in roads:
            pi = findAns(i)
            pj = findAns(j)
            parent[pj] = pi
            min_dis[pi] = min(min_dis[pi], min_dis[pj], dis)

        return min_dis[findAns(1)]
