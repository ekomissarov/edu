def genf1(f):
    def newfun(*args, **kwars):
        print("before run func...")
        res = f(*args, **kwars)
        print("after run func...")
        return res
    return newfun
    
@genf1
def fun1(a, b):
    print("running fun")
    return 2*a+b
    
print(fun1(2,3))
print("\n\n\n\n")




def repeat_num(times):
    def genf1(f):
        def newfun(*args, **kwars):
            print("before run func...")
            res = f(*args, **kwars)
            print("after run func...")
            return [res for _ in range(times)]
        return newfun
    return genf1

@repeat_num(5)
def fun2(a, b):
    print("running fun")
    return 2*a+b
    
print(fun2(2,3))
print("\n\n\n\n")




class Timer:
    from time import time
    from sys import stderr

    def __init__(self, fun):
        self.function = fun

    def __call__(self, *args, **kwargs):
        start_time = self.time()
        result = self.function(*args, **kwargs)
        end_time = self.time()
        print(f"Duration: {end_time-start_time} seconds", file=self.stderr)
        return result


# adding a decorator to the function
@Timer
def payload(delay):
    return sorted(sum(range(i)) for i in range(delay))

print(payload(10000)[-1])
print("\n\n\n\n")




def braced(cls):
    cls.___str_old = cls.__str__
    cls.__str__ = lambda x: "[[" + cls.___str_old(x) + "]]"
    return cls

@braced
class B(int):
    pass

b = B(24)
print(b) 
print("\n\n\n\n")




def braced_inherit(cls):
    class brac(cls):
        def __str__(self):
            return f"[[{super().__str__()}]]"
    return brac

@braced_inherit
class B(int):
    pass

b = B(24)
print(b) 
