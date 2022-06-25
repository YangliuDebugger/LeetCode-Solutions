class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # 模拟, 易错题，边界条件挺多的
        def calcost(L):
            if len(L) != 5:
                return 999999999999
            begin = False
            cost = 0
            for i in range(1, 5):
                if L[i] == '0' and not begin:
                    continue
                if not begin:
                    L[i - 1] = L[0]
                begin = True
                cost += pushCost
                if L[i] != L[i - 1]:
                    cost += moveCost
            return cost

        seconds = targetSeconds % 60
        minutes = targetSeconds // 60
        seconds = str(seconds)
        if len(seconds) == 1:
            seconds = '0' + seconds
        minutes = str(minutes)
        if len(minutes) == 1:
            minutes = '0' + minutes
        cost1 = calcost(list(str(startAt) + minutes + seconds))
        print(minutes + seconds, cost1)

        seconds = targetSeconds % 60
        minutes = targetSeconds // 60
        if seconds <= 39 and minutes >= 1:
            seconds += 60
            minutes -= 1
        seconds = str(seconds)
        if len(seconds) == 1:
            seconds = '0' + seconds
        minutes = str(minutes)
        if len(minutes) == 1:
            minutes = '0' + minutes
        cost2 = calcost(list(str(startAt) + minutes + seconds))
        print(minutes + seconds, cost2)
        return min(cost1, cost2)



