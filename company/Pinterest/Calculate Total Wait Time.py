import heapq

class Solution:
    def calculateWaitTime(self, N, M, T):
        L = [[0, i] * N for i in range(N)]
        for _ in range(M):
            heapq.heapreplace(L, [L[0][0]+T[L[0][1]], L[0][1]])
        return L[0][0]

solution = Solution()
print(solution.calculateWaitTime(2, 4, [4, 5]))