class Solution:
    def numberOfWays(self, s: str) -> int:
        ss = s
        s = [0,0,0,0,0,0] # 0,1,01,10,010,101
        # dp的题目，递推
        for i in ss:
            if i == '0':
                s = [s[0]+1,s[1],s[2],s[3]+s[1],s[4]+s[2],s[5]]
            else:
                s = [s[0],s[1]+1,s[2]+s[0],s[3],s[4],s[5]+s[3]]
            # print(s)
        return s[4] + s[5]