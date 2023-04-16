import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        acc = [0] * (len(w) + 1)
        for idx, weight in enumerate(w):
            acc[idx + 1] = acc[idx] + weight
        total = acc[-1]
        self.acc = [weight / total for weight in acc]

    def pickIndex(self) -> int:
        rand = random.random()
        idx = bisect.bisect_left(self.acc, rand)
        return max(0, idx - 1)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()