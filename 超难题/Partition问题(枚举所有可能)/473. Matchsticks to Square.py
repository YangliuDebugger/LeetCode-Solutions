class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        L = [0] * 4
        matchsticks.sort(reverse=True)
        ss = sum(matchsticks)
        if ss % 4 != 0:
            return False
        target = ss // 4
        self.find = False

        def enumerate(idx, fill_idx):
            if self.find:
                return
            if idx == len(matchsticks):
                self.find = True
            else:
                for i in range(0, fill_idx + 1):
                    if L[i] + matchsticks[idx] > target:
                        continue
                    L[i] += matchsticks[idx]
                    if i == fill_idx and fill_idx < 3:
                        enumerate(idx + 1, fill_idx + 1)
                    else:
                        enumerate(idx + 1, fill_idx)
                    L[i] -= matchsticks[idx]

        enumerate(0, 0)
        return self.find