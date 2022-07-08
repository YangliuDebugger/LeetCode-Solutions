class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # 这道题和2305一模一样，但是一样的代码不能通过是因为2305的代码里面没有最优化剪枝
        L = [0] * k
        self.global_min = sum(jobs)
        # jobs.sort(reverse=True)
        def enumerate(idx, fill_idx):
            if idx == len(jobs):
                self.global_min = min(self.global_min, max(L))
            else:
                for i in range(0, fill_idx + 1):
                    # 最优化剪枝
                    if L[i] + jobs[idx] > self.global_min:
                        continue
                    L[i] += jobs[idx]
                    if i == fill_idx and fill_idx < k - 1:
                        enumerate(idx + 1, fill_idx + 1)
                    else:
                        enumerate(idx + 1, fill_idx)
                    L[i] -= jobs[idx]

        enumerate(0, 0)
        return self.global_min

    # 论坛里的方法，bsearch可以是upper bound下降的更快，实际上会更加快
    def minimumTimeRequired(self, jobs, k):
        A = jobs
        n = len(A)
        A.sort(reverse=True)  # opt 1

        def dfs(i):
            if i == n: return True  # opt 3
            for j in range(k):
                if cap[j] >= A[i]:
                    cap[j] -= A[i]
                    if dfs(i + 1): return True
                    cap[j] += A[i]
                if cap[j] == x: break  # opt 2
            return False

        # binary search
        left, right = max(A), sum(A)
        while left < right:
            x = (left + right) // 2
            cap = [x] * k
            if dfs(0):
                right = x
            else:
                left = x + 1
        return left