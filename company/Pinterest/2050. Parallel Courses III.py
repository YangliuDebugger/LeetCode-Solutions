class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        outdegrees = {}
        indegree = {}
        max_pre_cost = time[:]
        for s, e in relations:
            s, e = s-1, e-1
            if s not in outdegrees:
                outdegrees[s] = []
            outdegrees[s].append(e)
            if e not in indegree:
                indegree[e] = 0
            indegree[e] += 1
        start_nodes = outdegrees.keys() - indegree.keys()
        from collections import deque
        q = deque()
        for node in start_nodes:
            q.append(node)
        # print(q)
        while q:
            x = q.popleft()
            # print(x)
            if x not in outdegrees:
                continue
            for next_node in outdegrees[x]:
                # print(x, next_node)
                max_pre_cost[next_node] = max(max_pre_cost[next_node], max_pre_cost[x] + time[next_node])
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
        return max(max_pre_cost)
