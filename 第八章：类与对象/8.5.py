#   计算属性然后缓存下来

# 描述器？

class lazyproperty:

    def __init__(self,func):
        self.func = func

    def __get__(self,instance,cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance,self.func.__name__,value)
            return value

import math

class Circle:
    def __init__(self,raduis):
        self.raduis = raduis
    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.raduis ** 2
    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.raduis
