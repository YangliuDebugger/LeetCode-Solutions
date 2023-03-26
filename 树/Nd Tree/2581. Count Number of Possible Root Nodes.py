class NDtree:
    def __init__(self, val) -> None:
        self.val = val
        self.children = []


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # 首先这是一个nd树，一旦root确定，所有节点的父子关系也就确定了
        G = [[] for i in range(len(edges) + 1)]
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        guess = set([tuple(i) for i in guesses])
        self.good = 0
        self.valid = 0

        # build tree and count how many correct guess
        def buildTree(node, parent_val):
            for i in G[node.val]:
                if i == parent_val:
                    continue
                if (node.val, i) in guess:
                    self.good += 1
                child = NDtree(i)
                node.children.append(child)
                buildTree(child, node.val)

        root = NDtree(0)
        buildTree(root, -1)

        # 2nd iteration to find valid root
        def walkTree(node, valid_cnt):
            if valid_cnt >= k:
                self.valid += 1
            for child in node.children:
                t = valid_cnt
                if (node.val, child.val) in guess:
                    t -= 1
                if (child.val, node.val) in guess:
                    t += 1
                walkTree(child, t)

        walkTree(root, self.good)
        return self.valid














