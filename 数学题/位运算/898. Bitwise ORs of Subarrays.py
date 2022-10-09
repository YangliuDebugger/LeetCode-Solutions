# 经典时间复杂度分析: https://leetcode.com/problems/bitwise-ors-of-subarrays/solutions/165881/c-java-python-o-30n/
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # 维护一个set， 记录到目前的idx为止有哪些值， 然后让新的和他们一一去取or
        d = set()
        s = set()
        for i in arr:
            ts = set()
            ts.add(i)
            for m in s:
                ts.add(m | i)
            d |= ts
            s = ts
        return len(d)
