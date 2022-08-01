class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # BFS 求最短路径
        N = len(edges) + 10

        def dfs(start_node):
            dis = [N] * len(edges)
            cnt = 0
            visit = set([start_node])
            dis[start_node] = 0
            while edges[start_node] != -1 and edges[start_node] not in visit:
                cnt += 1
                dis[edges[start_node]] = cnt
                start_node = edges[start_node]
                visit.add(start_node)
            return dis

        dis0 = dfs(node1)
        dis1 = dfs(node2)

        x = N
        best_node = -1
        for idx, (i, j) in enumerate(zip(dis0, dis1)):
            if max(i, j) < x:
                x = max(i, j)
                best_node = idx
        if x == N:
            return -1
        return best_node
