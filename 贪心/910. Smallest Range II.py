class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        L = nums[-1] - nums[0]
        C = []
        D = [i-k for i in nums[::-1]] # 把原来的数组都减去k，然后变成可以把一些元素加上2k
        N = len(D)
        for i in range(N-1):
            z = D.pop()
            C.append(z + 2 * k)  # 最需要加上2k的肯定是从小开始算起，不断枚举
            L = min(L, max(D[0],C[-1]) - min(D[-1],C[0])) # 实时计算当前数组中的最大值和最小值分别是多少
        return L