class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            t = list(str(num)[1:])
            t.sort(reverse=True)
            return -int(''.join(t))
        elif num > 0:
            zeros = ''
            num = list(str(num))
            num.sort()
            res = []
            for i in num:
                if i == '0':
                    zeros+=i
                else:
                    res.append(i)
                    if zeros:
                        res.append(zeros)
                        zeros = ''
            return ''.join(res)
        else:
            return 0