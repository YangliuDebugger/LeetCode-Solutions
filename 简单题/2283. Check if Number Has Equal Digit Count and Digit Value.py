class Solution:
    def digitCount(self, num: str) -> bool:
        D = {}
        for i in num:
            if i not in D:
                D[i] = 0
            D[i] += 1
        print(D)
        for idx, i in enumerate(num):
            if int(i) == 0:
                if str(idx) in D:
                    return False
            else:
                if str(idx) in D and D[str(idx)] == int(i):
                    continue
                else:
                    # print(i, D[i])
                    return False
        return True
