#!/usr/bin/env python
#http://ru.stackoverflow.com/questions/383679/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D0%BE%D0%B2%D1%82%D0%BE%D1%80%D1%8F%D1%8E%D1%89%D0%B8%D1%85%D1%81%D1%8F-%D1%81%D1%82%D1%80%D0%BE%D0%BA
#Ахо-Корасик-подобный алгоритм
import re # сопоставление с шаблонами, регулярные выражения
import sys # предоставляет доступ к компонентам системного окружения
from collections import Counter 

def main():
    # load substrings from file2
    with open('file2', 'rb') as file2: #rb для чтения двоичных данных без преобразования разрывов строк
        '''
        open возвращает объект поддерживающий протокол управления контекстом.
        Действия протокола при завершении работы, будут выполнены не зависимо от того сгенерируется исключение
        во время open или нет
        '''
        substrings = {line.strip() for line in file2} # unique lines
        '''
        используя иттератор строк файлового объекта
        создает множество строк с удаленными начальными и концевыми пробелами
        '''
        substrings = filter(None, substrings) # filter blank lines
        '''
        встроенная функция filter(функция, иттерируемый объект). Возвращает те элементы, для которых функция принимает истинное значение.
        Функция должна принимать 1 параметр. Если она указана None, то элементы просто проверяются на истинность.
        filter возвращает иттерируемый объект (формирующий значение по требованию и допускающий обход только 1 раз).
        этот иттерируемый объект можно преобразорвать в список используя list(), (но будет занимать память).
        '''
        substrings = sorted(substrings, key=len, reverse=True) # longest first
        '''
        встроенная функция. принимает иттерируемый объект.
        key - функция 1 аргумента используется для вычисления сравнительного значения из каждого элемента списка
        возвращает список
        '''
        pattern = b"|".join(map(re.escape, substrings))
        '''
        map применяет re.escape ко всем членам иттерируемого объекта и возвращает объект map
        re.escape - возвращает строку со всеми символами не являющимися буквенно цифровыми,
            но снабженными знаками оратной косой черты, 
            чтобы их можно было скомпилировать как строковой литерал
        объединяет байтовые строки с разделителем |
        '''
        find_substrings = re.compile(pattern).findall
        '''
        компилирует в шаблон pobj
        и присваевает функции findall со скомпилированным шаблоном новое имя
        '''

    # count substrings in file1
    counter = Counter()
    counter_update = counter.update # cache the lookup (for CPython)
    with open('file1', 'rb') as file1:
        for line in file1:
            tmp = find_substrings(line) # получаем список(list) совпадений с регулярными выражениями
            print('debug:', tmp)
            counter_update(tmp) # добавляем совпадения в счетчик

    # write substrings frequencies
    write = getattr(sys.stdout, 'buffer', sys.stdout).write
    for substring, count in counter.most_common(): # most common first
        write(substring)
        write(b' ')
        write(str(count).encode())
        write(b'\n')

main()
