# https://www.1point3acres.com/bbs/thread-957371-1-1.html

class Solution:
    def cross(self, l1, l2):
        if len(l1) == 0:
            return l2
        l = set()
        for i in l1:
            for j in l2:
                l.add(i+j)
        return l

    def braceExpansionII(self, expression: str) -> List[str]:
        # recusively
        def findDisStr(s):
            L = set()
            current_list = set()
            left_cnt = 0
            left_idx = -1
            for idx, i in enumerate(s):
                if i == '{':
                    if left_cnt == 0:
                        left_idx = idx
                    left_cnt += 1
                elif i == '}':
                    left_cnt  -= 1
                    if left_cnt == 0:
                        sub_list = findDisStr(s[left_idx+1:idx])
                        # print(s, s[left_idx+1:idx], current_list, sub_list)
                        current_list = self.cross(current_list, sub_list)
                elif i == ',':
                    if left_cnt == 0:
                        L = L | current_list
                        current_list = set()
                else:
                    if left_cnt == 0:
                        current_list = self.cross(current_list, set(i))
            L = L | current_list
            return L
        ans = findDisStr(expression)
        return sorted(list(ans))
