class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def mono1():
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
            return True

        def mono2():
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    return False
            return True

        return mono1() or mono2()