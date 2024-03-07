class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # double pointer
        start = 0
        end = 0
        cnt = 0
        cursum = 0
        while start < len(nums):
            while end < len(nums) and (cursum + nums[end]) * (end-start+1) < k:
                cursum += nums[end]
                end += 1
            cnt += (end - start)
            if nums[start] < k:
                cursum -= nums[start]
            start += 1
            end = max(start, end)
            # print(start, end, cnt, cursum)
        return cnt