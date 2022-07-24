class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        d={}
        for num in nums:
            x = bin(num)[2:].count('1')
            if x not in d:
                d[x] = 0
            d[x] += 1
        # print(d)
        cnt = 0
        for i in d:
            for j in d:
                if i + j >= k:
                    cnt += d[i] * d[j]
                    # if i == j:
                    #     cnt -= d[i]
        return cnt