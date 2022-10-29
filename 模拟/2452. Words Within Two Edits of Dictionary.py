class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # 数据规模这么小？
        res = []
        for q in queries:
            for w in dictionary:
                cnt = 0
                for z1, z2 in zip(q, w):
                    if z1 != z2:
                        cnt += 1
                if cnt <= 2:
                    res.append(q)
                    break
        return res
