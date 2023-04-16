class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxx = 0
        x = divisors[0]
        for i in divisors:
            cnt = 0
            for j in nums:
                if j % i == 0:
                    cnt += 1
            if cnt > maxx:
                maxx = cnt
                x = i
            elif cnt == maxx:
                x = min(x, i)
        return x