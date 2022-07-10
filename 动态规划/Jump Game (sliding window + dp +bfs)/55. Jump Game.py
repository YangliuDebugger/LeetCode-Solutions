class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # always keep the rightmost possible boundary
        rightmost = 0
        for idx, i in enumerate(nums):
            if rightmost < idx:
                return False
            rightmost = max(rightmost, idx + i)
            if rightmost >= len(nums) -1:
                return True