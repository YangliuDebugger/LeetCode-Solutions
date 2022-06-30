class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # 辗转相除法
        if num1 < num2:
            num1, num2 = num2, num1
        cnt = 0
        while num2 != 0:
            cnt += num1 // num2
            num1, num2 = num2, num1 % num2
        return cnt
