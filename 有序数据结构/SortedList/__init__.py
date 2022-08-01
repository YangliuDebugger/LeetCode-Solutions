"""
What is SortedList, It is a list that is always sorted from low to high.
Operation cost:

底层实现: 平衡搜索树

添加值
SortedList.add(value) 添加新元素，并排序。时间复杂度O(log(n)).
SortedList.update(iterable) 对添加的可迭代的所有元素排序。时间复杂度O(k*log(n)).
移除值
SortedList.clear() 移除所有元素。时间复杂度O(n).
SortedList.discard(value) 移除一个值元素，如果元素不存在，不报错。时间复杂度O(log(n)).
SortedList.remove(value) 移除一个值元素，如果元素不存在，报错ValueError。时间复杂度O(log(n)).
SortedList.pop(index=-1) 移除一个指定下标元素，如果有序序列为空或者下标超限，报错IndexError. 时间复杂度O(log(n)).
可以pop(0) 最小值，或者pop(-1)最大值

按index直接索引，像普通python的list一样，这个时间复杂度也是O(log(n))

总而言之，写查删都是O(log(n)),
相比于最小堆，写是log(O(n))，查是O(1), 没有办法删


SortedSet 和 SortedDict 其实都是类似的思想
SortedSet: 相当于没有重复元素的SortedList
SortedDict: 相当于字典的key值是按照sortedSet 来组织的
"""