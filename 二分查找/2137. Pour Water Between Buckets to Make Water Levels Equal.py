class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        # bsearch 的题？
        # 因为通过无穷等比数列，总是可以把每个桶都弄得一样， 这就保证high 可以
        # 的话，任何low < high 也一定可以，二分就完事了
        def Validate(x):
            left = 0
            for i in buckets:
                if x >= i:
                    left -= (x - i)
                else:
                    left += (i - x) * (100 - loss) / 100
            if left >= 0:
                return True

        thresh = 0.1 ** 5 * 0.5

        def bsearch(low, high):
            if high - low < thresh:
                return high

            mid = (low + high) / 2
            if Validate(mid):
                return bsearch(mid, high)
            return bsearch(low, mid)

        return bsearch(0, 10 ** 5)


