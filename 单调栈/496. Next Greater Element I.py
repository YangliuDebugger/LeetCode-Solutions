class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 单调栈
        res = {}
        res[nums2[-1]] = -1
        stack = [nums2[-1]]
        for i in range(len(nums2) - 2, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            res[nums2[i]] = -1
            if stack:
                res[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        return [res[i] for i in nums1]