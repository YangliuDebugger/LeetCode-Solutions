class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        import collections
        start, end = min(nums), max(nums)
        pluscost = 0
        currentcost = 0
        d = collections.defaultdict(list)
        for idx, i in enumerate(nums):
            d[i].append(idx)
            currentcost += (i - start) * cost[idx]
            if i == start:
                pluscost += cost[idx]
            else:
                pluscost -= cost[idx]
        # intialize
        best_cost = currentcost
        for i in sorted(d.keys())[1:]:
            currentcost += pluscost * (i - start)
            start = i
            best_cost = min(best_cost, currentcost)
            # if len(d[i]) != 0:
            for idx in d[i]:
                pluscost += 2 * cost[idx]
        return best_cost
