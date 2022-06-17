from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        for w in words[1:]:
            if sorted(list(res[-1])) == sorted(list(w)):
                continue
            res.append(w)
        return res
