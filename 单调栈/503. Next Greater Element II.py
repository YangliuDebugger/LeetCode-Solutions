# 循环数组一般都是复制一遍加在后面
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 单调栈
        nums = nums + nums
        res = [-1] * len(nums)
        stack = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])

        return res[:len(nums)//2]