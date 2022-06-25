class Solution:
    def minimumSum(self, num: int) -> int:
        minmin = num
        num = list(str(num))
        num.sort()
        L = [int(i) for i in num]
        for i in range(999):
            for j in range(999):
                if len(str(i)) + len(str(j)) > 4:
                    break
                t = str(i) + str(j)
                while len(t) < 4:
                    t = '0' + t
                t = list(t)
                t.sort()
                if t == num:
                    minmin = min(minmin, i + j)
        return minmin

