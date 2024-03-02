from collections import defaultdict
class Solution:
    def wordReconstruction(self, wordList):
        # construct grpah
        degree = defaultdict(int)
        graph = {}
        for word in wordList:
            s, e = word.split(">")
            if s not in graph:
                graph[s] = []
            if e not in graph:
                graph[e] = []
            graph[s].append([e, 0])
            degree[s] = degree[s] - 1
            degree[e] = degree[e] + 1

        start_point = wordList[0][0]
        count = [0, 0, 0]  # [0, 1, -1]
        for ch in degree:
            if degree[ch] < -1 or degree[ch] > 1:
                return ""  # invalid
            if degree[ch] == -1:
                start_point = ch
            count[degree[ch]] += 1
        if not ((count[1] == 1 and count[-1] == 1) or (count[1] == 0 and count[-1] == 0)):
            return ""  # invalid
        self.find = False
        self.path = [start_point]
        self.ans = ""

        # print(start_point)

        def dfs(ch, l):
            # print(ch, l)
            if self.find:
                return
            if l == len(wordList):
                self.find = True
                self.ans = "".join(self.path)

            for idx in range(len(graph[ch])):
                # print(idx, graph[ch], graph[ch][idx][0])
                if graph[ch][idx][1] == 0:  # not visit
                    # print("enter")
                    graph[ch][idx][1] = 1
                    self.path.append(graph[ch][idx][0])
                    dfs(self.path[-1], l+1)
                    self.path.pop()
                    graph[ch][idx][1] = 0

        dfs(start_point, 0)
        return self.ans

solution = Solution()
print(solution.wordReconstruction(["l>e", "e>t", "t>t", "t>e", "e>r"]))
