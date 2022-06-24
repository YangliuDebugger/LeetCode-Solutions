# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        Nodes = {}
        Children = set()
        for p,c,isleft in descriptions:
            if p not in Nodes:
                Nodes[p] = TreeNode(p)
            if c not in Nodes:
                Nodes[c] = TreeNode(c)
            if isleft == 1:
                Nodes[p].left = Nodes[c]
            else:
                Nodes[p].right = Nodes[c]
            Children.add(c)
        root = list((Nodes.keys() - Children))[0]
        return Nodes[root]