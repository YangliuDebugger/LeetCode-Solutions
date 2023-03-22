# https://www.1point3acres.com/bbs/thread-957371-1-1.html

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # prefix tree
        root = {}
        # build tree
        for w in words:
            d = root
            for c in w:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['#'] = '#'

        @cache
        def Findword(s, top_word):
            # print(s, top_word)

            # top_word = True means the first word, we need at leat two words for concat
            if s == '':
                return True
            d = root
            find = False
            for idx, c in enumerate(s):
                if c not in d:
                    break
                d = d[c]
                if '#' in d:
                    if idx == len(s) - 1 and top_word:
                        continue
                    find = find or Findword(s[idx + 1:], False)
            # print(s, top_word, find)

            return find

        # Findword('ratcatdogcat', True)

        L = []
        for w in words:
            if Findword(w, True):
                L.append(w)
        return L
