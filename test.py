import typing
from collections.abc import Iterable


def get_all_str(items: typing.List) ->None:
    for item in items:
        if isinstance(item, Iterable):
            yield from item
        else:
            yield item


a = [1, [2, 3, 1, 2], 'ss', ['aa', 'bb'], 'dca', ['a', 'c']]

for i in get_all_str(a):a
    print(i)
