class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        n = len(parent)
        L = [[] for _ in range(n)]
        for idx, i in enumerate(parent):
            if idx == 0:
                continue
            L[i].append(idx)

        def buildTree(node_idx, parent_idx):
            total_sum, total_node = value[node_idx], 1
            for child in L[node_idx]:
                if i != parent:
                    sum_node, num_node = buildTree(child, node_idx)
                    total_node += num_node
                    total_sum += sum_node
            if total_sum == 0:
                return 0, 0
            return total_sum, total_node

        _, res = buildTree(0, 0)
        return res




