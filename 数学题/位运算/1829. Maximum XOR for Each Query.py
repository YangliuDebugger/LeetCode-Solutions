class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        t = 0
        for i in nums:
            t ^= i
        res=[]
        x = 2 ** maximumBit - 1
        for i in nums[::-1]:
            res.append((((t >> maximumBit) << maximumBit) + x) ^ t)
            t ^= i
        return res