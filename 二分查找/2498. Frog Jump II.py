class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # besearh 的题目，choose + validation
        def validation(k):
            green_idx = 0
            red_idx = 0
            for idx in range(len(stones)):
                if green_idx <= red_idx:
                    if stones[idx] - stones[green_idx] > k:
                        return False
                    green_idx = idx
                else:
                    if stones[idx] - stones[red_idx] > k:
                        return False
                    red_idx = idx
            return True

        def besearh(low, high):
            if high - low <= 1:
                if validation(low):
                    return low
                return high
            mid = (low + high) // 2
            if validation(mid):
                return besearh(low, mid)
            return besearh(mid, high)

        return besearh(1, stones[-1] - stones[0])


