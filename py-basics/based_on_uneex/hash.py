print(hash("any python object"))  # в разных сессиях Python разные значения
print(hash("any python object"))
print(hash("any python object"))

print(hash((1,2,3)))
# хешировать имеет смысл только константные объекты
# для изменяемых объектов существуют хешируемые frozen аналоги

# множества в питоне - это суть хэш таблицы
a = {1, 2, 3, 4, 5, 6, 7}
print(a, type(a))  # set - это множество

