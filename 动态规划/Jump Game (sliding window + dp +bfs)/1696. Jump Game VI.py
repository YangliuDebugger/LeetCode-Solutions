class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # 看起来是一个dp的问题，但是肯定不能直接做，因为时间复杂度
        # 变成O(n^2), n = 10^5应该承受不住
        # 再次观察，发现是维护长度为k的滑动窗口的最大值
        n = len(nums)
        dp = [0] * n
        max_index = 0
        dp[0] = nums[0]
        for i in range(1, n):
            # print (dp)
            if i - max_index <= k:
                dp[i] = dp[max_index] + nums[i]
                if nums[i] >= 0:  # 更新新的max_index, 过去k以内最大的dp对应index
                    max_index = i
            else:
                max_index = -1
                m = -100000000000
                for j in range(max(0, i - k), i):
                    if dp[j] >= m:
                        max_index = j
                        m = dp[j]
                dp[i] = dp[max_index] + nums[i]
                if nums[i] >= 0:
                    max_index = i
        return dp[-1]

