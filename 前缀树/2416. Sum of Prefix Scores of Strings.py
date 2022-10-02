class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # 定义一个这么奇怪的score 算法无非就是想套用特定的数据结构比如说 prefix tree
        D = {}
        for word in words:
            d = D
            for w in word:
                if w not in d:
                    d[w] = [{}, 0]
                d[w][1] += 1
                d = d[w][0]

        res = []
        for word in words:
            cnt = 0
            d = D
            for w in word:
                cnt += d[w][1]
                d=d[w][0]
            res.append(cnt)
        return res
