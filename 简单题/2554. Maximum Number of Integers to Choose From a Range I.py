class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        c = 0
        i = 0
        cnt = 0
        while i < n:
            i += 1
            if i in banned:
                continue
            if c + i <= maxSum:
                cnt += 1
                c += i
            else:
               break
        return cnt