class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        L = [[] for i in range(n)]
        for s, e in edges:
            L[s].append(e)
            L[e].append(s)

        visit = set(restricted)
        visit.add(0)
        cnt = 0
        q = [0]
        while q:
            tq = []
            for i in q:
                # print(i)
                cnt += 1
                for j in L[i]:
                    if j not in visit:
                        tq.append(j)
                        visit.add(j)
            q = tq
        return cnt