class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # 在于pair统计的转换，什么时候统计了2次，数学算两次的思想
        t = [i - j for i, j in zip(nums1, nums2)]
        t.sort(reverse=True)
        cnt = 0
        start = 0
        end = len(t) - 1
        while start < end:
            while start < end and t[start] + t[end] <= 0:
                end -= 1
            if start >= end:
                break
            cnt += end - start
            start += 1
        return cnt
