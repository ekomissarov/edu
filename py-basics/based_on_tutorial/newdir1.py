# учебный скрипт ===
# Выводит результат dir() в виде словаря {id, лист названий}, уникализация по id
dirList = {id(eval(i)):list() for i in dir()}
for i in dir():
    if id(eval(i)) in dirList.keys():
        dirList[id(eval(i))].append(i)
        # eval интерпретирует строку как команду Python в текущем пространстве имен

print("{")
for i in dirList:
    print(i, dirList[i], sep=': ')
print("}")
