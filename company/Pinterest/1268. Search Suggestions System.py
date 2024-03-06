class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        D = {}
        self.res = []
        self.cur = []

        def buildTrie(wordList):
            for word in wordList:
                d = D
                for ch in word:
                    if ch not in d:
                        d[ch] = {}
                    d = d[ch]
                d['#'] = '#'

        buildTrie(products)

        def dfs(d):
            if len(self.res) == 3:
                return
            if '#' in d:
                self.res.append(''.join(self.cur))
            for ch in sorted(d.keys()):
                if ch == '#':
                    continue
                self.cur.append(ch)
                dfs(d[ch])
                self.cur.pop()

        ans = []
        d = D
        pre = ""
        for ch in searchWord:
            self.res = []
            if ch not in d:
                ans.append([])
                d = {}  # all the longer prefix will return empty
                continue
            d = d[ch]
            pre += ch
            self.cur = [pre]
            dfs(d)
            ans.append(self.res[:])
        return ans

