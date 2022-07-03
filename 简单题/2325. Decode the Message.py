class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        s = "abcdefghijklmnopqrstuvwxyz"

        cnt = 0
        for i in key:
            if i == ' ':
                continue
            if i not in d:
                d[i] = s[cnt]
                cnt += 1
                if cnt == 26:
                    break
        res = []
        for i in message:
            if i == ' ':
                res.append(i)
            else:
                res.append(d[i])
        return ''.join(res)

