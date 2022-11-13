class Solution:
    def nextGreaterElement(self, n: int) -> int:
        number = str(n)
        i = len(number) - 1
        if ''.join(sorted(number, reverse=True)) == number:
            return -1
        while i >= 0 and ''.join(sorted(number[i:], reverse=True)) == number[i:]:
            i -= 1

        best_idx, best_n = -1, 'a'
        tmp_array = [j for j in number[i:]]
        for idx, x in enumerate(tmp_array):
            if x > tmp_array[0]:
                if x < best_n:
                    best_idx, best_n = idx, x

        tmp_array = tmp_array[:best_idx] + tmp_array[best_idx + 1:]

        m = int(number[:i] + best_n + ''.join(sorted(tmp_array)))

        if m <= 2 ** 31 - 1:
            return m
        return -1
