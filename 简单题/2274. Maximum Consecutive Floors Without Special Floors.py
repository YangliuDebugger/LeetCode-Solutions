from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special = special + [bottom-1, top+1]
        special.sort()
        cnt = 0
        for idx in range(1, len(special)):
            cnt = max(cnt, special[idx] - special[idx-1]-1)
        return cnt
