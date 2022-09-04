class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        for idx, i in enumerate(queries):
            s = 0
            cnt = 0
            for j in nums:
                if s + j <= i:
                    s += j
                    cnt += 1
                else:
                    break
            res.append(cnt)
        return res
