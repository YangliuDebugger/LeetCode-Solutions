# Big O analysis is always O(n^3), need to apply some trick to prune
# 最优化剪枝和可行性剪枝

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # brute force
        degree = {}
        cnt = [0] * (n+1)
        for i in range(1, n+1):
            degree[i] = set()
        for i, j in edges:
            degree[i].add(j)
            degree[j].add(i)
            cnt[i] += 1
            cnt[j] += 1
        best = 10 ** 9
        for i in range(1, n+1):
            for j in sorted(list(degree[i]), reverse=True):
                if i >= j:
                    break
                for k in sorted(list(degree[i] & degree[j]), reverse=True):
                    if j >= k:
                        break
                    best = min(best, cnt[i] + cnt[j] + cnt[k] - 6)
        if best == 10 ** 9:
            return -1
        return best