# 双端队列 + 2个哈希表， 巧妙的用cnt来处理移除的问题（异步移动节点）

class LRUCache:
    def __init__(self, capacity):
        self.cnt = collections.defaultdict(int)
        self.cap = capacity
        self.q = collections.deque()
        self.d = {}

    def get(self, key):
        if key not in self.d:
            return -1
        self.cnt[key] += 1
        self.q.append(key)
        return self.d[key]

    def put(self, key, val):
        self.cnt[key] += 1
        self.q.append(key)
        self.d[key] = val
        # 注意这里是测试字典的长度，而不是deque的长度，deque本身可以非常长（就只盯着同一个元素薅）
        while len(self.d) > self.cap:
            k = self.q.popleft()
            self.cnt[k] -= 1
            if self.cnt[k] == 0:
                del self.cnt[k]
                del self.d[k]