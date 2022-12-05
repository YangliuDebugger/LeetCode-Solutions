class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        s.append(s[0])
        for i in range(1, len(s)):
            if s[i-1][-1] != s[i][0]:
                return False
        return True