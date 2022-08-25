
class String:
    def __init__(self,name):
        self.name = name

    def __get__(self,instance,cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self,instance,value):
        if not isinstance(value,str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value


class Person:
    name = String('name')

    def __init__(self,name):
        self.name = name


class SubPerson(Person):

    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self,value):
        print('Setting name to',value)
        super(SubPerson, self).name.__set__(self,value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, self).name.__delete__(self)

class SubPerson1(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().names

