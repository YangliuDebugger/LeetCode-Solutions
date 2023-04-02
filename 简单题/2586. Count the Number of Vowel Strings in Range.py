class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        d = set('aeiou')
        print(d)
        cnt = 0
        for i in range(left, right+1):
            if words[i][0] in d and words[i][-1] in d:
                cnt += 1
        return cnt