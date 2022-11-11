# 双向链表 + 哈希表

class DoublyListnode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.last = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cnt = 0
        self.head = DoublyListnode(0, 0)
        self.tail = self.head

        self.D = {}

    def move_last(self, node):
        if node != self.tail:
            node.last.next, node.next.last = node.next, node.last
            self.tail.next, node.last, node.next = node, self.tail, None
            self.tail = node

    def get(self, key: int) -> int:
        if key in self.D:
            # update position in the linked list
            self.move_last(self.D[key])
            return self.D[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.D:
            self.D[key].value = value
            self.move_last(self.D[key])
        else:
            new_node = DoublyListnode(key, value)
            self.D[key] = new_node
            self.tail.next, new_node.last, new_node.next = new_node, self.tail, None
            self.tail = self.tail.next
            self.cnt += 1
            if self.cnt > self.capacity:
                self.cnt -= 1
                head_key = self.head.next.key
                del self.D[head_key]
                self.head.next = self.head.next.next
                self.head.next.last = self.head
                # not sure why we cannot do it at the same time, maybe the time Python
                # try to find refernce
                # self.head.next, self.head.next.next.last = self.head.next.next, self.head

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)