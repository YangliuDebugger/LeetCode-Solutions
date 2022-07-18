class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        import math
        t = numsDivide[0]
        for i in numsDivide:
            t = math.gcd(t, i)
        nums.sort()
        for idx, i in enumerate(nums):
            if t % i == 0:
                return idx
        return -1
