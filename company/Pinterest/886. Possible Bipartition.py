class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        L = [[] for _ in range(n + 1)]
        for s, e in dislikes:
            L[s].append(e)
            L[e].append(s)

        color = [-1] * (n + 1)

        def dfs(node, i):
            color[node] = i
            for nei in L[node]:
                if color[nei] == -1:
                    if not dfs(nei, 1 - i):
                        return False
                elif color[nei] == 1 - i:
                    continue
                else:
                    return False
            return True

        for i in range(1, n + 1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True

