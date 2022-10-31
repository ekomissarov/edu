'''

    A.v
   | \
   B  C.v
   \ |
    D

https://www.python.org/download/releases/2.3/mro/
'''

class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass

print(D.__mro__)  # любая более сложная зависимость будет линеаризована
# и поиск методов будет происходить именно по этой цепочке


class A1: pass
class B1(A1): pass
class B2(A1): pass
class C1(B1,B2): pass
class C2(B1,B2): pass # class C2(B2,B1): pass так работать не будет, т.к. алгоритм mro
# не сможет построить линеаризацию
class D1(C1,C2): pass

print(D1.__mro__)



# метод наследования
class Int(int):
    def __add__(self, other):
        return type(self)(int.__add__(self, other))

i,j = Int(9), Int(80)
print(i+j, type(i+j))



# метод проксирования
class INt:
    def __init__(self, *val):
        self.val = int(*val)
    def __add__(self, other):
        return type(self)(self.val + other.val)
# только не будет работать ни умножение ни деление ничего
# нужно делать полное проксирование (исп. getatribute и т.п.)
# читать статьи проксирование vs наследование в python



class Int2(Int):
    def __mul__(self, other):
        #return type(self)(???.__mul__(self, other))
        # мнение1: ??? писать тот класс от которого мы унаследовались благо он один
        # мнение2: ??? писать тот класс в котором на самом деле объявлен метод
        # мнение3: мы никогда без анализа кода в сложном коде не знаем ответа на эти 2 вопроса
        # кто-то за нас должен динамически вычислять
        return type(self)(super().__mul__(other))
        #super это именно обращение к процедуре mro с выстраиванием и проходом по
        #линеаризованному графу наследования и выяснению чей же метод мы берем
        #super(type(self)), self) почему пропущено?
        #почему __mul__(self, other), self опущен?


i, j = Int2(9), Int2(80)
print("#####", type(i*j))

print(super(Int2, i))
print(super(Int2, i).__add__) # метод класса Int (c большой буквы)

print(super(Int2, i).__mul__) # метод wrapper взят из самого базового объяекта, мы его не переопределяли
print(super(Int2, i).__sub__)

