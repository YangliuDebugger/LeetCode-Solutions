class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num + 1):
            if int(str(i)[::-1]) + i == num:
                return True
        return False
