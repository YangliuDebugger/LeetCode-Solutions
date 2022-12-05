class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = sum(skill) * 2
        if s % len(skill) != 0:
            return -1
        s //= len(skill)
        d = collections.defaultdict(int)
        prod = 0
        cnt = 0
        for i in skill:
            if d[s-i] > 0:
                prod += i * (s-i)
                d[s-i] -= 1
                cnt += 2
            else:
                d[i] += 1
        if cnt == len(skill):
            return prod
        return -1

