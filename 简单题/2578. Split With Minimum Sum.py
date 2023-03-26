class Solution:
    def splitNum(self, num: int) -> int:
        num = [int(i) for i in str(num)]
        if len(num) % 2 == 1:
            num.append(0)
        num.sort()
        num1 = [str(i) for idx, i in enumerate(num) if idx%2 == 0]
        num2 = [str(i) for idx, i in enumerate(num) if idx%2 == 1]
        return int(''.join(num1)) + int(''.join(num2))