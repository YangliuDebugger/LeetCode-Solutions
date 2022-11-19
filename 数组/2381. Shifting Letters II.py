# 其实就是range addition
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # accumulate array, range addition
        n = len(s)
        shift = [0] * (n+1) # shift[i] = x means all characters after index i will be shifted forward by x
        maxc = ord('z')
        for i, j, k in shifts:
            shift[i] += (k * 2 - 1)
            shift[j+1] -= (k *  2 - 1)
        res = []
        accumulate = 0
        for idx, val in enumerate(shift[:-1]):
            accumulate += val
            c = ord(s[idx]) + accumulate % 26
            if c > maxc:
                c -= 26
            res.append(chr(c))
        return ''.join(res)
