from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # 简单，按照位把不同的数group在一起: log(10000000) / log(2) = 23.25
        d = {2**k: 0 for k in range(25)}
        for i in candidates:
            for key in d:
                if i & key > 0:
                    d[key] += 1
        return max(d.values())