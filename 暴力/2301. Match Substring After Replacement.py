# 类型: 模拟O(MN)，理论上KMP应该能解决which is O(M+N)

from typing import List


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        # 非优化的KMP, 时间复杂度最高为 5000 * 1000，但是还是可以接受的
        d = {}
        for c in sub:
            d[c] = set(c)
        for start, end in mappings:
            if start not in d:
                d[start] = set(start)
            d[start].add(end)
        idx_0 = 0
        l0, l1 = len(s), len(sub)
        # print(idx_0,l1,l0)
        while idx_0 + l1 <= l0:
            # print(idx_0)
            bad_match = False
            for i in range(l1):
                if s[idx_0 + i] not in d[sub[i]]:
                    bad_match = True
                    break
            idx_0 += 1
            if bad_match:
                continue
            return True
        return False
