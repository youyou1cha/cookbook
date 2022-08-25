import logging

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:

    def __get__(self,instance,obj_type=None):
        value = instance._age
        logging.info('Accessing %r giving %r', 'age',value)
        return value

    def __set__(self, instance, value):
        logging.info('Updating %r to %r','age',value)
        instance._age = value

class Person:
    age = LoggedAgeAccess()

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

if __name__ == '__main__':
    mary = Person('Marm',30)
    mary.birthday()