class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = [str(i) for i in mapping]
        nums = [(int(''.join([mapping[int(j)] for j in str(num)])), idx, num) for idx, num in enumerate(nums)]
        nums.sort()
        # print(nums)
        return [i[2] for i in nums]
