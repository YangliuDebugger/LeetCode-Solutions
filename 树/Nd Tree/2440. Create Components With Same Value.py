class TreeNode:
    def __init__(self, idx, parent_idx):
        self.idx = idx
        self.parent_idx = parent_idx
        self.children = []


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        # 好像是一个n-d tree的遍历就可以解决，题目提示了当做树来做

        M = defaultdict(list)
        for s, e in edges:
            M[s].append(e)
            M[e].append(s)

        # buld N-d tree
        root = TreeNode(0, -1)

        def build_tree(node):
            for nei in M[node.idx]:
                if nei != node.parent_idx:
                    child_node = TreeNode(nei, node.idx)
                    node.children.append(child_node)
                    build_tree(child_node)

        build_tree(root)

        # 判读一个M划分是否，即每个component的sum都是M
        self.valid = True

        def valid_tree(node, M):
            child_sum = 0
            for child_node in node.children:
                child_sum += valid_tree(child_node, M)
            if child_sum + nums[node.idx] > M:
                self.valid = False
            return (child_sum + nums[node.idx]) % M

        ss, mm = sum(nums), max(nums)
        for i in range(mm, ss):
            if ss % i == 0:
                self.valid = True
                valid_tree(root, i)
                if self.valid:
                    return ss // i - 1
        return 0




