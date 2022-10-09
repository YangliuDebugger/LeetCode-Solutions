class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # 数学题
        d = [1]
        t = 1
        cnt = 0
        n = str(n)
        for i in range(len(n)):
            d.append(d[-1] * len(digits))
            cnt += d[-1]
        cnt -= d[-1]
        # 开始处理与n有相同位数时有多少partial的count
        idx = 0
        while idx < len(n):
            iidx = 0
            while iidx < len(digits) and digits[iidx] < n[idx]:
                cnt += d[-idx-2]
                iidx += 1
            # 情况1，所有的数字都比当前位数小
            if iidx == len(digits):
                return cnt
            # 情况2， 不存在平票的情况
            if digits[iidx] > n[idx]:
                return cnt
            idx += 1
        # 最特殊的情况
        if n[-1] == digits[iidx]:
            cnt += 1
        return cnt
