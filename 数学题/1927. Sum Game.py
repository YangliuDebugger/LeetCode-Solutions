class Solution:
    def sumGame(self, num: str) -> bool:
        left_cnt = 0
        right_cnt = 0
        left_sum = 0
        right_sum = 0

        for i in num[:len(num) // 2]:
            if i == "?":
                left_cnt += 1
            else:
                left_sum += int(i)

        for i in num[len(num) // 2:]:
            if i == "?":
                right_cnt += 1
            else:
                right_sum += int(i)

        # Alice 尽可能往多的加9，少的补0
        # Bob则相反
        if left_sum <= right_sum:
            left_sum, right_sum = right_sum, left_sum
            left_cnt, right_cnt = right_cnt, left_cnt

        print(left_sum, right_sum, left_cnt, right_cnt)

        # left_sum >= right_sum
        if left_cnt > right_cnt:
            return True
        if left_cnt == right_cnt:
            return not (left_sum == right_sum)

        # 这一块的逻辑最复杂
        # left_cnt < right_cnt
        cnt_diff = right_cnt - left_cnt
        if cnt_diff % 2 == 1:
            return True
        # 同余问题，类似一次只能报1个数和2个数，谁先报到30谁赢的必胜策略
        return not (left_sum - right_sum == (cnt_diff // 2) * 9)