class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window
        start = 0
        end = 0
        cnt = 0
        d = collections.defaultdict(int)
        maxx = 0
        while end < len(fruits):
            while end < len(fruits):
                d[fruits[end]] += 1
                if d[fruits[end]] == 1:
                    cnt += 1
                if cnt > 2:
                    d[fruits[end]] -= 1
                    cnt -= 1
                    break
                end += 1

            maxx = max(maxx, end - start)
            while cnt > 1:
                d[fruits[start]] -= 1
                if d[fruits[start]] == 0:
                    cnt -= 1
                start += 1
        return maxx