
def calculateTarget(target, numbers):
    from collections import deque
    q = deque()
    q.append((target, len(numbers)))
    while q:
        val, idx = q.popleft()
        if idx == 0:
            if val == 0:
                return True
            else:
                continue
        if val % numbers[idx-1] == 0:
            q.append((val // numbers[idx-1], idx-1))
        q.append((val - numbers[idx-1], idx-1))
    return False

print(calculateTarget(21, [1,2,3,4]))


