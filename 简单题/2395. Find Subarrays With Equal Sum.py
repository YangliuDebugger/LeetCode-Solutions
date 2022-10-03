class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        d = set()
        for i in range(len(nums)-1):
            s = nums[i] + nums[i+1]
            if s not in d:
                d.add(s)
            else:
                return True
        return False