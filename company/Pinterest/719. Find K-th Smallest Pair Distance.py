class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        mm = nums[1] - nums[0]
        for idx in range(1, len(nums)):
            mm = min(mm, nums[idx] - nums[idx - 1])

        def countArray(val):
            start = 0
            end = 1
            cnt = 0
            while start < len(nums):
                while end < len(nums) and nums[end] - nums[start] < val:
                    end += 1
                cnt += end - start - 1
                start += 1
                end = max(start + 1, end)
            return cnt

            # print(countArray(4))

        # return 0

        def bsearch(low, high):
            if high - low <= 1:
                if countArray(high) > k - 1:
                    return low
                return high

            mid = (low + high) // 2
            x = countArray(mid)

            print(low, high, mid, x)

            if x >= k:
                return bsearch(low, mid)
            return bsearch(mid, high)

        return bsearch(mm, nums[-1] - nums[0])
