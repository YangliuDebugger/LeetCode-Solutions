from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # 数学公式转换
        # (nums1[i] - nums2[i]) - (nums1[j] - nums2[j]) <= diff.
        t = [i-j for i,j in zip(nums1, nums2)]
        x = SortedList(t)
        cnt = 0
        l = len(t)
        for i in t:
            l -= 1
            x.remove(i)
            cnt += l - x.bisect_left(i-diff)
        return cnt
