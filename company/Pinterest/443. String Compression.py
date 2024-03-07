class Solution:
    def compress(self, chars: List[str]) -> int:
        slow = 0
        cnt = 0
        for idx, ch in enumerate(chars):
            if idx == 0:
                cnt = 1
                continue

            if ch == chars[idx - 1]:
                cnt += 1
            else:
                chars[slow] = chars[idx - 1]
                slow += 1
                if cnt > 1:
                    cnt = str(cnt)
                    for iidx in range(len(cnt)):
                        chars[slow] = cnt[iidx]
                        slow += 1
                cnt = 1

        chars[slow] = chars[idx]
        slow += 1
        if cnt > 1:
            cnt = str(cnt)
            for iidx in range(len(cnt)):
                print(chars, slow)
                chars[slow] = cnt[iidx]
                slow += 1
        cnt = 1
        # print(slow, cnt, chars, ch, chars[idx-1])
        return slow