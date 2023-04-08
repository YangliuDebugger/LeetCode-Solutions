import bisect


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        t = [0] * len(nums)
        t[0] = sum(nums) - nums[0] * len(nums)
        for idx, i in enumerate(nums):
            if idx == 0:
                continue
            t[idx] = t[idx-1] + (2 * idx - len(nums)) * (nums[idx] - nums[idx-1])
        res = []
        for q in queries:
            x = bisect.bisect_left(nums, q)
            if x == len(nums):
                res.append(t[-1] + (q - nums[-1]) * len(nums))
            # elif x == 0:
            #     res.append(t[0] + (nums[0] - q) * len(nums))
            else:
                # nums[x] == q 可以合并
                # x == 0, (t[0] + (nums[0] - q) * len(nums)) 也可以合并

                # 从右边或者左边过去都可以
                # print(t[x] + (len(nums) - 2 * x) * (nums[x] - q))
                # print(t[x-1] + (2 * x - len(nums)) * (q - nums[x-1]))
                res.append(t[x] + (len(nums) - 2 * x) * (nums[x] - q))
        return res


