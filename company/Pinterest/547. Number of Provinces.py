class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # union-find
        def findAncestor(x):
            if parent[x] != x:
                parent[x] = findAncestor(parent[x])
            return parent[x]

        n = len(isConnected)
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    parent_i = findAncestor(i)
                    parent_j = findAncestor(j)
                    parent[parent_i] = parent_j

        for i in range(n):
            findAncestor(i)

        return len(set(parent))

