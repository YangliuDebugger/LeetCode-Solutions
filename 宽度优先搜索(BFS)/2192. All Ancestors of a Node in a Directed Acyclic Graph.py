class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # BFS
        indegree = [0] * n
        matrix = [[] for _ in range(n)]
        for i, j in edges:
            indegree[j] += 1
            matrix[i].append(j)

        L = []
        res = [set() for _ in range(n)]
        for idx, i in enumerate(indegree):
            if i == 0:
                L.append(idx)
        while L:
            tL = []
            for i in L:
                for j in matrix[i]:
                    indegree[j] -= 1
                    res[j] = (res[j] | res[i])
                    res[j].add(i)
                    if indegree[j] == 0:
                        tL.append(j)
            L = tL
        # print(res)
        return [sorted(list(i)) for i in res]
