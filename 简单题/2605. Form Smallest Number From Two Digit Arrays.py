class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        m = nums1[0] * 10 + nums2[0]
        for i in nums1:
            for j in nums2:
                if i == j:
                    m = min(m, i)
                else:
                    m = min(i*10+j, j*10+i, m)
        return m