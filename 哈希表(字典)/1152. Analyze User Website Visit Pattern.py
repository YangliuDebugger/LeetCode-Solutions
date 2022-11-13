class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # 找出最common公共子序列？这个序列只有3的长度
        users = {}
        for user, time, web in zip(username, timestamp, website):
            if user not in users:
                users[user] = []
            users[user].append((time, web))

        # we can enumerate every possible combination
        d = {}
        best_cnt = 0
        best_s = ''
        for user in users:
            visit = set()
            users[user].sort()
            for i in range(len(users[user])-2):
                for j in range(i+1, len(users[user])-1):
                    if users[user][j][0] == users[user][i][0]:
                        continue
                    for k in range(j+1, len(users[user])):
                        if users[user][j][0] == users[user][k][0]:
                            continue
                        s = users[user][i][1] + ',' + users[user][j][1] + ',' + users[user][k][1]
                        if s not in d:
                            d[s] = 0
                        if s not in visit:
                            d[s] += 1
                            visit.add(s)
        print(users)
        print(d)

        for i in d:
            if d[i] > best_cnt:
                best_cnt = d[i]
                best_s = i
            elif d[i] == best_cnt:
                best_s = min(best_s, i)
        x = best_s.split(",")
        return x
