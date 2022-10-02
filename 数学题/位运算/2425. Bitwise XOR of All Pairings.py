class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # 计算每个元素在最后会出现几次，因为每两次都会变成一个0
        x = 0
        if len(nums2) % 2 == 1:
            for i in nums1:
                x ^= i
        if len(nums1) % 2 == 1:
            for i in nums2:
                x ^= i
        return x