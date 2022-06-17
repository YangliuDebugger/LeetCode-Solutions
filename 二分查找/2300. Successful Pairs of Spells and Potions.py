# 类型: 二分查找

from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # bsearch
        import bisect
        potions.sort()
        res = []
        N = len(potions)
        for spell in spells:
            x = bisect.bisect_left(potions, success/spell)
            res.append(N - x)
        return res
