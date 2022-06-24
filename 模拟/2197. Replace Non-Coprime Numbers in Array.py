def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if not res:
                res.append(i)
                continue
            res.append(i)
            while len(res) > 1:
                t = gcd(res[-1], res[-2])
                if t != 1:
                    res[-2] = res[-1] * res[-2] // t
                    res.pop()
                else:
                    break
        return res
