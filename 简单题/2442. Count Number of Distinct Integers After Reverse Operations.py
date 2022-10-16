class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        t = [int(str(i)[::-1]) for i in nums] + nums
        return len(set(t))