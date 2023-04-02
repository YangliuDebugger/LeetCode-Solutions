class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # 这个subarray 所有的element进行bit位计数，每一位上的和是偶数就可以了
        # 更进一步，就是亦或 ^ , 需要这个subarray全员异或后为0
        # 这样就可以变成一个hash table的问题
        d = {0:1}
        cur = 0
        cnt = 0
        for i in nums:
            cur ^= i
            if cur not in d:
                d[cur] = 0
            cnt += d[cur]
            d[cur] += 1
        return cnt
