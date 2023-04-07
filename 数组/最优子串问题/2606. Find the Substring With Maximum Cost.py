class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cost={}
        for idx, i in enumerate("abcdefghijklmnopqrstuvwxyz"):
            cost[i] = idx + 1
        for i, c in zip(chars, vals):
            cost[i] = c
        best = 0
        cur_cost = 0
        for i in s:
            if cur_cost + cost[i] >= 0:
                cur_cost += cost[i]
            else:
                cur_cost = 0
            best = max(best, cur_cost)
        return best