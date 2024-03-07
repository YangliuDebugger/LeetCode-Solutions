class Solution:
    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split("+")
        number1 = [(int(max(num1[:idx], "1")), int(num1[idx:]), idx) for idx in range(len(num1))]
        number2 = [(int(num2[:idx]), int(max(num2[idx:], "1")), idx) for idx in range(1, len(num2) + 1)]

        # print(number1, number2)
        min_res = int(num1) + int(num2)
        min_idx1 = 0
        min_idx2 = len(num2)

        # print(min_res)

        for num1_1, num1_2, idx1 in number1:
            for num2_1, num2_2, idx2 in number2:
                res = num1_1 * (num1_2 + num2_1) * num2_2
                # print(num1_1, num1_2, num2_1, num2_2, res)
                if res < min_res:
                    min_res = res
                    min_res, min_idx1, min_idx2 = res, idx1, idx2

        # print(min_res)
        if min_idx1 == 0:
            num1_res = "(" + num1
        else:
            num1_res = num1[:min_idx1] + "(" + num1[min_idx1:]

        if min_idx2 == len(num2):
            num2_res = num2 + ")"
        else:
            num2_res = num2[:min_idx2] + ")" + num2[min_idx2:]

        return num1_res + "+" + num2_res