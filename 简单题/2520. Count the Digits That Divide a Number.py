class Solution:
    def countDigits(self, num: int) -> int:
        cnt = 0
        for i in list(str(num)):
            if num % int(i) == 0:
                cnt += 1
        return cnt