class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if(b == 0):
                return abs(a)
            else:
                return gcd(b, a % b)
        cnt = 0
        for start in range(len(nums)):
            x = nums[start]
            for end in range(start, len(nums)):
                x = gcd(x, nums[end])
                if x == k:
                    cnt += 1
                elif x < k:
                    break
        return cnt