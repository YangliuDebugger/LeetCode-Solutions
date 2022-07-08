class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # 数据规模太小，枚举所有可能性, NP hard 问题
        # 复杂度(n * 3 ^ M)
        toppingCosts.sort(reverse=True)
        baseCosts.sort(reverse=True)
        self.best = baseCosts[0]

        def enumerate(idx, cur_cost):
            if idx == len(toppingCosts) + 1:
                if abs(cur_cost - target) == abs(self.best - target):
                    self.best = min(self.best, cur_cost)
                elif abs(cur_cost - target) < abs(self.best - target):
                    self.best = cur_cost
                return

            if idx == 0:
                for i in baseCosts:
                    if i - target <= abs(self.best - target):
                        enumerate(idx + 1, i)
            else:
                for j in range(3):
                    extra_cost = j * toppingCosts[idx - 1]
                    if cur_cost + extra_cost - target <= abs(self.best - target):
                        enumerate(idx + 1, cur_cost + extra_cost)

        enumerate(0, 0)
        return self.best