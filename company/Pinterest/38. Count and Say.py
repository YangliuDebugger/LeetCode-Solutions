class Solution:
    def countAndSay(self, n: int) -> str:
        cur = '1'
        while n > 1:
            print(n, cur)
            tmp = ""
            lastdigit = "-1"
            last_idx = 0
            for idx, c in enumerate(cur):
                if c != lastdigit:
                    if idx != last_idx:
                        tmp += (f"{(idx - last_idx)}" + lastdigit)
                    lastdigit = c
                    last_idx = idx
            tmp += (f"{(idx - last_idx + 1)}" + lastdigit)
            cur = tmp
            n -= 1
        return cur