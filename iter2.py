# 代理迭代

class Node:

    def __init__(self,value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self,node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

class test:
    def __init__(self,data=1):
        self.data = data
    def __iter__(self):
        return self
    def __next__(self):
        if self.data > 5:
            raise  StopIteration
        else:
            self.data += 1
            return self.data


# 紧盯用户，不要盯着竞争对手
# 做用户想的产品
# 输入什么输出什么

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child2)
    root.add_child(child1)

    for ch in root:
        print(ch)
    for item in test(3):
        print(item)