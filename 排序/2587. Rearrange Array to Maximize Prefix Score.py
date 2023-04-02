class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # 大的放前面
        nums.sort(key = lambda x: -x)
        cur = 0
        cnt = 0
        for ele in nums:
            cur += ele
            if cur > 0:
                cnt += 1
            else:
                break
        return cnt