class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # k1, k2可以合起来，没啥区别, 又是优先队列的问题
        # 没有注意到k1，k2有那么大，寄了，那应该是bsearch的问题
        import heapq
        K = k1 + k2
        L = [abs(i - j) for i, j in zip(nums1, nums2)]
        # bsearch搜索最小的最大差距可以是多少
        L.sort(reverse=True)

        def valid(n):
            cnt = 0
            for i in L:
                if i > n:
                    cnt += (i - n)
                if cnt > K:
                    return False
            return True

        def bsearch(low, high):
            if high - low <= 1:
                if valid(low):
                    return low
                return high
            mid = (low + high) // 2
            if valid(mid):
                return bsearch(low, mid)
            return bsearch(mid, high)

        minmax = bsearch(0, 10 ** 9)
        if minmax == 0:
            return 0
        for idx in range(len(L)):
            if L[idx] >= minmax:
                L[idx], K = minmax, K - (L[idx] - minmax)
            else:
                break
        result = 0
        for idx in range(len(L)):
            if K > 0:
                result += (L[idx] - 1) * (L[idx] - 1)
                K -= 1
            else:
                result += L[idx] * L[idx]
        return result








