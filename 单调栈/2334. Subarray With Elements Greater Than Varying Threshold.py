class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums = [threshold // i + 1 for i in nums]
        mono_stack = [[10 ** 12 + 1, -1]]  # 在-1初始化一个无法逾越的大山

        # 双边的mono stack，记录从i开始，nums[i]往左和往右分别能走多远
        left_span = [0] * len(nums)
        right_span = [0] * len(nums)
        for idx, i in enumerate(nums):
            while mono_stack[-1][0] <= i:
                mono_stack.pop()
            left_span[idx] = idx - mono_stack[-1][1]
            mono_stack.append([i, idx])

        mono_stack = [[10 ** 12 + 1, len(nums)]]  # 在len(nums)初始化一个无法逾越的大山
        for idx in range(len(nums) - 1, -1, -1):
            while mono_stack[-1][0] <= nums[idx]:
                mono_stack.pop()
            right_span[idx] = mono_stack[-1][1] - idx
            if left_span[idx] + right_span[idx] - 1 >= nums[idx]:
                return left_span[idx] + right_span[idx] - 1
            mono_stack.append([nums[idx], idx])
        return -1







