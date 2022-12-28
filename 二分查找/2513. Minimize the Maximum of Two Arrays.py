class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        # bsearch
        lcm = math.lcm(divisor1, divisor2)

        def validation(n):
            # 容斥原理
            # A: n // divisor1
            # B: n // divisor2
            # need: |!A| >= uniqueCnt1 and |!B| >= uniqueCnt2 and |!A U !B|  >= uniqueCnt1 + uniqueCnt2
            not_A = n - n // divisor1
            not_B = n - n // divisor2
            not_A_inter_B = n - n // lcm
            return not_A >= uniqueCnt1 and not_B >= uniqueCnt2 and not_A_inter_B >= uniqueCnt1 + uniqueCnt2

        left, right = 1, 10 ** 10
        while True:
            if right - left <= 1:
                if validation(left):
                    return left
                return right
            mid = (left + right) // 2
            if validation(mid):
                right = mid
            else:
                left = mid
