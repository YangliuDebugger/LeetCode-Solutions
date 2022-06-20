# 这个暴力做法会超出内存限制，看解法貌似要fenwick tree, merge sort, 区间树, etc

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Memory limit 爆了，咋优化？
        N = len(nums1)
        S1_L = [set() for i in range(N)]
        S2_L = [set() for i in range(N)]

        T_L = [0] * N
        T_R = [0] * N

        for i in range(1, N):
            S1_L[nums1[i]] = S1_L[nums1[i - 1]] | set([nums1[i - 1]])
            S2_L[nums2[i]] = S2_L[nums2[i - 1]] | set([nums2[i - 1]])

        full_set = set([i for i in range(N)])

        cnt = 0
        for i in range(N):
            # print(S1_L[i] & S2_L[i], i, S1_R[i] & S2_R[i])
            cnt += len(S1_L[i] & S2_L[i]) * (len((full_set - S1_L[i]) & (full_set - S2_L[i])) - 1)

        return cnt
