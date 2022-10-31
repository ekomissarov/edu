print("Глобальное пространство имен:", dir())
import math
print("Глобальное пространство имен после импорта модуля math:", dir())
print("Глобальное пространство имен самого модуля math:", dir(math))
from math import sin
print("Глобальное пространство имен после импорта функции sin модуля math:", dir())
print("Справка по функции sin")
print(help(sin))

a = 5
print("Все в Python это объект, даже функция", type(a), type(sin), id(a), id(sin))
a = sin
print("Их можно связывать разными именами", type(a), type(sin), id(a), id(sin))
print("a is sin:", a is sin)
from sys import getrefcount
print("Количество ссылок на объект можно посмотреть с помощью getrefcount", getrefcount(sin))

print("Поля и методы объекта описаны в пространстве имен этого объекта", dir(sin))
print("Объект функции отличается от просто объекта тем что в его пространстве имен есть метод __call__")
