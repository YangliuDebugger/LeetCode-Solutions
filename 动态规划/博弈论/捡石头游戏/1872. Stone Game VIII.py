class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # 看数据规模，10^5 显然不可以用O(n^2)的dp算法了
        # 暗示至少是是一个O(nlogn) 或者O(n)的算法
        # 因为我们会发现Alice合并后会把它们的sum还是放在最左边，对于bob来说
        # 合并还是不合并其实没有区别，因为是算从左边开始的sum
        # 所以这就变成了1维的dp

        N = len(stones)
        # dp = [-10**9] * (N+1)
        cursum = [0] * (N + 1)
        for idx in range(N):
            cursum[idx + 1] = cursum[idx] + stones[idx]

        maxx = cursum[N]
        for i in range(N - 1, 1, -1):  # 计算dp[i]，即现在最小的idx至少得取到i
            if cursum[i] - maxx > maxx:
                maxx = cursum[i] - maxx

            # for j in range(i+1, N+1): # 把 i 到 j-1的数全部取走，留下一个以j开始的序列
            #     dp[i] = max(dp[i], cursum[j] - dp[j])
            #     # 我们发现cursum[j] - dp[j] 不会变，所以可以直接记录下来

        return maxx