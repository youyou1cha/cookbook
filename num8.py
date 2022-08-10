#!/usr/bin/env python
# -*- coding: utf-8 -*-

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# 根据字段进行排序会出现，可以用lambda 也可以用operator itemgetter方法
# 排序的sorted 其实其实调用了callback方法，回调方法来获得字段。可以用lambda返回字典也可以用itemgetter返回
# 如果是多个字段排序，返回的额是元组

from operator import itemgetter, attrgetter
from itertools import groupby

row_by_fname = sorted(rows, key=itemgetter('fname'))
row_by_uid = sorted(rows, key=lambda r: r['fname'])


# 类似这个attrgetter 获取属性
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(21), User(11)]
    print(users)
    print(sorted(users, key=lambda s: s.user_id))
    print(sorted(users, key=attrgetter('user_id')))


if __name__ == '__main__':
    sort_notcompare()

# groupby
# gourpby 输入一个字典或者序列 返回一个关键字和迭代器。进行分组

rows111 = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows111.sort(key=itemgetter('date'))

for date,items in groupby(rows111,key=itemgetter('date')):
    print(date)
    for item in items:
        print(item)