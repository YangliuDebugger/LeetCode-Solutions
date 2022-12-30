class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # bsearch 的题目
        price.sort()

        def valid(taste):
            cnt = 1
            last_idx = 0
            for i in range(1, len(price)):
                if price[i] - price[last_idx] >= taste:
                    cnt += 1
                    last_idx = i
            return cnt >= k

        print(price)
        left = 0  # 题目描述有误，是可以有两个物品等价的
        right = price[-1] - price[0]
        while True:
            if right - left <= 1:
                if valid(right):
                    return right
                return left

            mid = (left + right) // 2
            if valid(mid):
                left = mid
            else:
                right = mid