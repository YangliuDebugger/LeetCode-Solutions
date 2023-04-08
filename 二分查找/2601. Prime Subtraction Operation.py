import bisect


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # 数据规模很小
        d = [1] * 1001
        d[0] = 0
        d[1] = 0
        L = []
        # 找素数
        for i in range(1001):
            if d[i] == 1:
                L.append(i)
                t = i * i
                while t <= 1000:
                    d[t] = 0
                    t += i
        last = 0
        for idx, i in enumerate(nums):
            if i <= last:
                return False
            x = bisect.bisect_left(L, i - last)
            if x > 0:
                last = i - L[x - 1]
            else:
                last = i
            # print(i, last, L[x])
        return True


