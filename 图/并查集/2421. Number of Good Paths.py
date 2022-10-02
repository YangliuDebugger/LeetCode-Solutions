class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # 按照value逐渐expand
        n = len(vals)
        L = [[] for _ in range(n)]
        # 构建邻接矩阵
        for s, t in edges:
            if vals[s] >= vals[t]:
                L[s].append(t)
            else:
                L[t].append(s)
        # 按照value 大小 aggregate node
        d = {}
        for idx, v in enumerate(vals):
            if v not in d:
                d[v] = []
            d[v].append(idx)

        total = 0
        # 初始化union find 需要的code
        parent = [i for i in range(n)]
        cnt = [0] * n
        current_component = []

        def getAns(idx):
            if parent[idx] != idx:
                parent[idx] = getAns(parent[idx])
            return parent[idx]

        for v in sorted(d.keys()):
            current_component = set()
            for node_idx in d[v]:
                Ans_idx = getAns(node_idx)
                if Ans_idx not in current_component:
                    current_component.add(Ans_idx)
                    cnt[Ans_idx] = 1
                else:
                    cnt[Ans_idx] += 1

                for neighbour in L[node_idx]:
                    left_ans = getAns(node_idx)
                    right_ans = getAns(neighbour)
                    if right_ans not in current_component:
                        cnt[right_ans] = 0

                    if left_ans < right_ans:
                        cnt[left_ans] += cnt[right_ans]
                        current_component.add(left_ans)
                        current_component.discard(right_ans)
                        parent[right_ans] = left_ans
                    elif left_ans > right_ans:
                        cnt[right_ans] += cnt[left_ans]
                        current_component.add(right_ans)
                        current_component.discard(left_ans)
                        parent[left_ans] = right_ans

            # print(v, parent, current_component)

            for idx in current_component:
                total += cnt[idx] * (cnt[idx] + 1) // 2
        return total





