#!/usr/bin/env python
# -*- coding: utf-8 -*-

# heap为min_heap 根节点是最小值
class PriorityQueueBase:
    # 基类抽象

    class Item:
        __slots__ = '_key','_value'

        def __init__(self,k,v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

        def is_empty(self):
            return len(self) == 0

        def __str__(self):
            return set(self._key)

class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = [ ]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def add(self,key,value):
        self._data.append(self.Item(key,value))

    def min(self):
        if self.is_empty():
            raise  ValueError('Priority queue is empty')
        item = self._data[0]
        return (item._key,item._value)

    def remove_min(self):
        if self.is_empty():
            raise  ValueError('Priority queue is empty')
        self._swap(0,len(self._data) - 1 )
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

    def _parent(self,j):
        return (j - 1 )// 2

    def _upheap(self,j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j,parent)
            self._upheap(parent)

    def _swap(self,i,j):
        self._data[i],self._data[j] = self._data[j],self._data[i]

    def _left(self,j):
        return 2 * j + 1

    def _right(self,j):
        return 2 * j + 2

    def _has_right(self,j):
        return self._right(j) < len(self._data)

    def _has_left(self,j):
        return self._left(j) < len(self._data)

    def _downheap(self,j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right()
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j,small_child)
                self._downheap(small_child)