class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # 感觉可以分别拓扑排序row and col, tp sort
        def tp_sort(arr):
            indegree = [0] * (k + 1)
            outnode = {i: [] for i in range(k + 1)}
            for i, j in arr:
                indegree[j] += 1
                outnode[i].append(j)
            q = []
            for idx, i in enumerate(indegree):
                if idx == 0:
                    continue
                if i == 0:
                    q.append(idx)
            res_order = []
            while q:
                tq = []
                for i in q:
                    res_order.append(i)
                    for s in outnode[i]:
                        indegree[s] -= 1
                        if indegree[s] == 0:
                            tq.append(s)
                q = tq
            if len(res_order) == k:
                return res_order
            return []

        col_order = tp_sort(colConditions)
        row_order = tp_sort(rowConditions)

        # print(col_order)
        # print(row_order)

        if len(col_order) == 0 or len(row_order) == 0:
            return []

        xy = [[-1, -1] for i in range(k + 1)]

        M = {}

        for idx, i in enumerate(row_order):
            xy[i][0] = idx

        for idx, i in enumerate(col_order):
            xy[i][1] = idx
            M[(xy[i][0], xy[i][1])] = i

        res = [[0] * k for i in range(k)]
        for i in range(k):
            for j in range(k):
                if (i, j) in M:
                    res[i][j] = M[(i, j)]

        return res











