class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visit = [0] * len(arr)

        def dfs(node):
            visit[node] = 1
            if node + arr[node] < len(arr) and visit[node + arr[node]] == 0:
                dfs(node + arr[node])
            if node - arr[node] >= 0 and visit[node - arr[node]] == 0:
                dfs(node - arr[node])

        dfs(start)

        for idx, v in enumerate(arr):
            if v == 0 and visit[idx] == 1:
                return True
        return False


