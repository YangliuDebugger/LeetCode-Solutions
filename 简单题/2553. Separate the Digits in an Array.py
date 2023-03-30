class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(j) for j in list(''.join([str(i) for i in nums]))]