class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # bsearch + partiton
        tasks.sort(reverse=True)
        self.L = [0] * len(tasks)

        @cache
        def isValid(num_sessions):
            self.L = [0] * num_sessions
            self.find = False
            enumerate(0, 0, num_sessions)
            return self.find

        def enumerate(idx, fill_idx, num_sessions):
            if self.find:
                return
            if idx == len(tasks):
                self.find = True
            else:
                for i in range(0, fill_idx + 1):
                    if self.L[i] + tasks[idx] > sessionTime:
                        continue
                    self.L[i] += tasks[idx]
                    if i == fill_idx and fill_idx < num_sessions - 1:
                        enumerate(idx + 1, fill_idx + 1, num_sessions)
                    else:
                        enumerate(idx + 1, fill_idx, num_sessions)
                    self.L[i] -= tasks[idx]

        def bsearch(left, right):
            if right - left <= 1:
                if isValid(left):
                    return left
                return right

            mid = (left + right) // 2
            if isValid(mid):
                return bsearch(left, mid)
            return bsearch(mid, right)

        return bsearch(1, len(tasks))