# 鸭子行为
# __repr__
# __str__
# __format__

_formats = {
    'ymd': '{d.year}--{d.month}-{d.year}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}
class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair{0.x!r},{0.y!r}'.format(self)

    def __str__(self):
        return '({0.x!s},{0.y!s})'.format(self)