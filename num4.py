# 字典中的键多个值

from collections import  defaultdict

d1 = defaultdict(list)
d2 = defaultdict(set)
d1['a'].append(1)
d1['a'].append(2)
d1['b'].append(3)

d2['a'].add(1)
d2['a'].add(2)
d2['b'].add(3)

d = {}
d.setdefault('a',[]).append(1)

d = {}

for key,value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

d = defaultdict(list)
for key,value in pairs:
    d[key].append(value

# 排序的字典OrderedDict DefualtDict