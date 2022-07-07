class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        # D = {} # represent the optimal (start, end)
        n = len(stones)
        D = [[-1] * (n+1) for _ in range(n+1)]
        cumsum = [0] * (n+1)
        for idx, val in enumerate(stones):
            cumsum[idx+1] = cumsum[idx] + val
        # print (cumsum)
        def FindOptima(start, end):
            if start == end:
                return 0
            if D[start][end] == -1:
                leftdiff = (cumsum[end+1] - cumsum[start+1]) - FindOptima(start+1, end)
                rightdiff = (cumsum[end] - cumsum[start]) - FindOptima(start, end-1)
                D[start][end] = max(leftdiff, rightdiff)
            return D[start][end]
        return FindOptima(0, n-1)