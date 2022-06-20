class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        t = sum(nums)
        cnt = 0
        left = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= t - left:
                # print(i)
                cnt += 1
        return cnt
