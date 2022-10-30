class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        a = 0
        for i in nums:
            if i % 6 == 0:
                s += i
                a += 1
        if a == 0:
            return 0
        return s // a
