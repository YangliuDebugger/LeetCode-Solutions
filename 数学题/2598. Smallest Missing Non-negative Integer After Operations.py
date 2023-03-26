class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # group by remainder
        z = [0] * value
        for i in nums:
            r = i % value
            z[r] += 1
        mm = min(z)
        for idx, i in enumerate(z):
            if i == mm:
                return mm * value + idx
