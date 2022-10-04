class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # 树形dp
        d = {}  # 记录该节点下最长单列，从入度为0的点开始走 (类似tp sort)
        n = len(s)
        indegree = [0] * n
        for p in parent[1:]:
            indegree[p] += 1
        L = []
        for idx, i in enumerate(indegree):
            if i == 0:
                L.append(idx)
        maxl = 1
        print(indegree)
        while L:
            tmpL = []
            for i in L:
                tL = 1
                if i in d:
                    d[i].sort()
                    if len(d[i]) >= 2:
                        maxl = max(maxl, 1 + d[i][-1] + d[i][-2])
                        tL = 1 + d[i][-1]
                    elif len(d[i]) == 1:
                        maxl = max(maxl, 1 + d[i][0])
                        tL = 1 + d[i][0]
                if parent[i] == -1:
                    # print(d)
                    return maxl
                if parent[i] not in d:
                    d[parent[i]] = []
                if s[i] != s[parent[i]]:
                    d[parent[i]].append(tL)
                indegree[parent[i]] -= 1
                if indegree[parent[i]] == 0:
                    tmpL.append(parent[i])

            L = tmpL

