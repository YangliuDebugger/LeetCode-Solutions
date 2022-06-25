# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = ListNode(0)
        cur = newhead
        cursum = 0
        head = head.next
        while head:
            if head.val == 0:
                cur.next = ListNode(cursum)
                cur = cur.next
                cursum = 0
            cursum += head.val
            head = head.next
        return newhead.next