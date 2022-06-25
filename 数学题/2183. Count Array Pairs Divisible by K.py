class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = [0] * (10 ** 5 + 1)
        for num in nums:
            for i in range(1, int(num ** 0.5) + 2):
                if num % i == 0:
                    if i < num / i:
                        count[i] += 1
                        count[num // i] += 1
                    elif i * i == num:
                        count[i] += 1
                        break

        @cache
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        # print(count)
        cnt = 0
        for num in nums:
            useful = gcd(k, num)
            left = k // useful
            cnt += count[left]
            if num % left == 0:  # very important
                cnt -= 1
        return cnt // 2
