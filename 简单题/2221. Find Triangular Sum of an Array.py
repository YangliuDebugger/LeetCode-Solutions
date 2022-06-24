class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        cnt = 1
        N = len(nums)
        while cnt < len(nums):
            # print(nums)
            for i in range(N-cnt):
                nums[i] = (nums[i] + nums[i+1]) % 10
            cnt += 1
        return nums[0]