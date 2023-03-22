# https://www.1point3acres.com/bbs/thread-948691-1-1.html

class Solution:
    def decodeString(self, s: str) -> str:
        # number followed by [
        def recursive_decode(s):
            decode = ''
            meet_digit = False
            digit_s_idx = -1
            digit_e_idx = -1
            mul = 0
            leftcnt = 0
            for idx, i in enumerate(s):
                if i.isdigit():
                    if meet_digit == False:
                        meet_digit = True
                        digit_s_idx = idx
                elif i == '[':
                    if leftcnt == 0:
                        mul = int(s[digit_s_idx:idx])
                        digit_e_idx = idx
                    leftcnt += 1
                elif i == ']':
                    leftcnt -= 1
                    if leftcnt == 0:
                        meet_digit = False
                        digit_idx = -1
                        decode = decode + mul * recursive_decode(s[digit_e_idx+1: idx])
                elif i.isalpha() and not meet_digit:
                    decode += i
            return decode
        return recursive_decode(s)