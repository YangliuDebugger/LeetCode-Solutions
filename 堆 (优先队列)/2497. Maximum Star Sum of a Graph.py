class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # every node maintains heap
        import heapq
        n = len(vals)
        L = [[] for _ in range(n)]
        for i, j in edges:
            if vals[j] > 0:
                heapq.heappush(L[i], vals[j])
            if vals[i] > 0:
                heapq.heappush(L[j], vals[i])
            if len(L[i]) == k+1:
                heapq.heappop(L[i])
            if len(L[j]) == k+1:
                heapq.heappop(L[j])
        return max([vals[i] + sum(L[i]) for i in range(n)])
