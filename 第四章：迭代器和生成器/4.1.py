#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 自定义实现迭代器，使用yiled或者iter
class Node:

    def __init__(self, value):
        self.value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        for i in self._children:
            yield i


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)

    for ch in root:
        print(ch)
