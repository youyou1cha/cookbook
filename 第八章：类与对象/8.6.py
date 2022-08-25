class Structure3:

    _fields = []

    def __init__(self,*args,**kwargs):

        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        for name,value in zip(self._fields,args):
            setattr(self,name,value)

        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self,name,kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicate value of {}'.format(','.join(kwargs)))