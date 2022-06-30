class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # sliding window, double pointer
        n = len(answerKey)
        if n<=2: return n
        global_max = 0
        for label in ['T', 'F']:
            # print('label:', label)
            cnt = 0
            start_idx = 0
            end_idx = start_idx
            # 分两次，T来一次，F来一次
            while end_idx < n and start_idx < n:
                # print('start:', start_idx, end_idx, cnt)
                while end_idx < n and cnt <= k:
                    if answerKey[end_idx] == label:
                        end_idx += 1
                    else:
                        if cnt < k:
                            cnt += 1
                            end_idx += 1
                        else:
                            break
                # print('end:', start_idx, end_idx, cnt)
                global_max = max(global_max, end_idx - start_idx)
                if answerKey[start_idx] != label:
                    cnt -= 1
                start_idx += 1
        return global_max