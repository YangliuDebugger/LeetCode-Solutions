class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res=[]
        accumulate = 0
        maxc = ord('z')
        for idx in range(len(s)-1, -1, -1):
            accumulate += shifts[idx]
            c = ord(s[idx]) + accumulate % 26
            if c > maxc:
                c -= 26
            res.append(chr(c))
        return ''.join(res[::-1])