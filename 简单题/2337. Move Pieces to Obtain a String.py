class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # 两步走
        seq1 = [i for i in start if i != '_']
        seq2 = [i for i in target if i != '_']
        # print(seq1, seq2)
        if seq1 != seq2:
            return False
        # target的L要比L更左，target的R要比start的R更右
        cnt_left = 0
        right_cnt = 0
        for i, j in zip(start, target):
            if j == 'L':
                cnt_left += 1
            if i == 'L':
                cnt_left -= 1
            if cnt_left < 0:
                return False
            if i == 'R':
                right_cnt += 1
            if j == 'R':
                right_cnt -= 1
            if right_cnt < 0:
                return False
        return True