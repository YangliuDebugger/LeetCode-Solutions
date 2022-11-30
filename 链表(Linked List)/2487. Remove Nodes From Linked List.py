# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # remove with dfs
        def dfs(node):
            if node.next:
                next_node = dfs(node.next)
                if node.val < next_node.val:
                    return next_node
                else:
                    node.next = next_node
                    return node
            return node

        return dfs(head)
