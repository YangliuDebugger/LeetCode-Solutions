class Solution:
    def longestWord(self, words: List[str]) -> str:
        # 前缀树+DFS巡游
        D = {}
        D['#'] = {}  # 边界条件
        for word in words:
            d = D
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['#'] = {}  # 表示有word结束于此

        self.word = []
        self.best = ''

        def dfs(d):
            if '#' in d:
                for key in d:
                    self.word.append(key)
                    dfs(d[key])
                    self.word.pop()
            else:
                if len(self.word) > len(self.best):
                    self.best = ''.join(self.word)
                elif len(self.word) == len(self.best):
                    self.best = min(self.best, ''.join(self.word))

        dfs(D)
        return self.best[:-1]  # 去掉尾部的 #
