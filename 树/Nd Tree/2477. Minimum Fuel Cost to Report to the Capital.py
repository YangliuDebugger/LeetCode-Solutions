class NDTreenode:
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # build N-d tree
        L = [[] for i in range(len(roads) + 1)]
        for i, j in roads:
            L[i].append(j)
            L[j].append(i)

        # one pass, build tree and find answer
        def buildTree(node, parent_node):
            total_seat, total_oil = 1, 0
            for nb in L[node.val]:
                if nb != parent_node.val:
                    node.children.append(NDTreenode(nb))
                    n_seat, oil = buildTree(node.children[-1], node)
                    total_seat, total_oil = total_seat + n_seat, total_oil + oil

            return total_seat, total_oil + (total_seat - 1) // seats + 1

        root = NDTreenode(0)
        total_seat, ans = buildTree(root, root)
        ans -= (total_seat - 1) // seats + 1
        return ans






