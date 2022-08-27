class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Generate all possible
        visit = [0] * 10
        self.R = []
        self.small = 100000000000

        def generateNum(idx):
            if idx - 1 == len(pattern):
                self.small = min(self.small, int(''.join([str(i) for i in self.R])))
                return
            for i in range(1, 10):
                if visit[i] == 0:
                    if idx > 0:
                        if pattern[idx - 1] == 'I' and i > self.R[-1]:
                            visit[i] = 1
                            self.R.append(i)
                            generateNum(idx + 1)
                            self.R.pop()
                            visit[i] = 0
                        if pattern[idx - 1] == 'D' and i < self.R[-1]:
                            visit[i] = 1
                            self.R.append(i)
                            generateNum(idx + 1)
                            self.R.pop()
                            visit[i] = 0
                    else:
                        visit[i] = 1
                        self.R.append(i)
                        generateNum(idx + 1)
                        self.R.pop()
                        visit[i] = 0

        generateNum(0)
        return str(self.small)


