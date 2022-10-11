class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # 维护到这个时间点为止，领先的人是谁
        S = set(persons)
        D = {}
        self.T = []
        self.P = []
        for i in S:
            D[i] = 0
        starttime = times[0]
        curidx = persons[0]
        curvotes = 1
        D[curidx] = 1
        N = len(times)
        for i in range(1, N):
            D[persons[i]] += 1
            if persons[i] == curidx:
                curvotes += 1
                continue
            else:
                if D[persons[i]] >= curvotes:  # change
                    self.T.append(starttime)
                    self.P.append(curidx)
                    starttime = times[i]
                    curidx = persons[i]
                    curvotes = D[persons[i]]
        self.T.append(starttime)
        self.P.append(curidx)

    def q(self, t: int) -> int:
        # 用二分查找去定位时间点
        z = bisect.bisect_left(self.T, t)
        # print z
        if z == len(self.T) or t < self.T[z]:
            z -= 1
        return self.P[z]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)