class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        increase = [0] * n
        decrease = [0] * n
        increase[0] = 1
        decrease[0] = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increase[i] = increase[i - 1] + 1
                decrease[i] = 1
            elif nums[i] < nums[i - 1]:
                decrease[i] = decrease[i - 1] + 1
                increase[i] = 1
            else:
                increase[i] = increase[i - 1] + 1
                decrease[i] = decrease[i - 1] + 1

        res = []
        for i in range(k, len(nums) - k):
            if decrease[i - 1] >= k and increase[i + k] >= k:
                res.append(i)
        return res