# 直接用orderedDict ()

import collections
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.q = collections.OrderedDict()

    def get(self, key):
        if key not in self.q:
            return -1
        self.q.move_to_end(key, last=True)
        return self.q[key]

    def put(self, key, val):
        self.q[key] = val
        self.q.move_to_end(key, last=True)
        while len(self.q) > self.cap:
            self.q.popitem(last=False)