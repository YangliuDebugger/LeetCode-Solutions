# 类型: 模拟

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        s = "!@#$%^&*()-+"
        little, big, num, repeat, spec = False, False, False, True, False
        for idx, i in enumerate(password):
            if 'a' <= i <= 'z':
                little = True
            if 'A' <= i <= 'Z':
                big = True
            if '0' <= i <= '9':
                num = True
            if i in s:
                spec = True
            if idx >= 1 and password[idx-1] == i:
                repeat = False
        return little & big & num & repeat & spec