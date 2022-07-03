# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for i in range(m)]
        x, y = 0, 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cnt = 0
        xx = m * n
        while head:
            res[x][y] = head.val
            head = head.next
            if not head:
                break
            nx, ny = x + direction[cnt][0], y + direction[cnt][1]
            while (not (0 <= nx < m and 0 <= ny < n)) or res[nx][ny] != -1:
                # print(nx, ny)
                cnt = (cnt + 1) % 4
                nx, ny = x + direction[cnt][0], y + direction[cnt][1]
            x, y = nx, ny
        return res
