from random import randrange
from functools import wraps

def fuck_int(cls):
    @wraps(cls)
    class remake_some(cls):
        def __add__(self, other):
            if randrange(10) == 0:
                return super().__add__(other) + 1
            else:
                return super().__add__(other)
    return remake_some


@fuck_int
class Int(int): pass

__builtins__.int = Int
del Int
del fuck_int
