class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        def gcd(a, b):
            if a < b:
                a, b = b, a
            if b == 0:
                return a
            return gcd(b, a % b)

        t = nums[0]
        cnt = 1
        for num in nums:
            x = gcd(t, num)
            if x == 1:
                cnt += 1
                t = num
            else:
                t = x
        return cnt