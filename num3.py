2  # !/usr/bin/env python
# -*- coding: utf-8 -*-

# 实现一个优先级队列
# 利用heapd 实现优先级队列
import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    # priority 保持负数，是优先级高到低
    # Index 是插入顺序
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

# 元组比对大小，先比较第一个然后比较第二个

if __name__ == '__main__':

    # test
    q = PriorityQueue()
    q.push(Item('foo'),1)
    q.push(Item('bar'),5)
    q.push(Item('spam'),5)
    q.pop()