class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        cnt = 0
        while start < end:
            if nums[start] == nums[end]:
                start += 1
                end -= 1
            elif nums[start] < nums[end]:
                start += 1
                nums[start] += nums[start-1]
                cnt += 1
            else:
                end -= 1
                nums[end] += nums[end+1]
                cnt += 1
        return cnt